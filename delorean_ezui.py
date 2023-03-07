import ezui

class Controller(ezui.WindowController):

    def build(self):
        self.fontsMap = dict()        
        for font in AllFonts():            
            name = f"{font.info.familyName} {font.info.styleName}"
            if name in self.fontsMap:
                print(f"Duplicated font: {name}")
            self.fontsMap[name] = font
        
        if not self.fontsMap:
            print("Open some fonts!!!")


        content = """         
        = VerticalStack
        * HorizontalStack               
            > ( ...)                    @fontSource1
            > ( ...)                    @fontSource2
        
        * HorizontalStack               
            > Glyph Name:
            > [_       _]               @glyphName
        
        * HorizontalStack
            > Interpolation:
            > ---X--- [__]              @interpolation         
         
        * Box                           @glyphPreviewBox
            > * RoboFontGlyphPreview    @glyphPreview
            
        ===        
        ( ⬇ )                          @generateGlyph
        """
        glyph = CurrentGlyph()
        
        currentGlyphName = ""
        if glyph is not None:
            currentGlyphName = glyph.name
            
        descriptionData = dict(   
            fontSource1=dict(
                width=150,
                items=self.fontsMap.keys()                
            ),
            fontSource2=dict(
                width=150,
                items=self.fontsMap.keys()
            ),
            glyphName=dict(
                width="fill",
                value=currentGlyphName
            ),
            interpolation=dict(
                value=0,
                minValue=-200,
                maxValue=400,
            ),
            glyphPreview=dict(
                height="fill",
                width="fill",
                glyph=glyph
            ),
        )
        self.w = ezui.EZWindow(
            title="Delorean: Interpolation Preview",
            content=content,
            descriptionData=descriptionData,
            size=(400, 400),
            minSize=(150, 150),
            controller=self
        )
        print(self.w.getItem("glyphPreview"))
    
    def started(self):
        self.w.open()
    
    def generateGlyphCallback(self, sender):
        print("genereate glyph!")
    
    def interpolationCallback(self, sender):
        factor = sender.get() / 100
        
        fontSource1 = self.w.getItem("fontSource1")
        fontSource2 = self.w.getItem("fontSource2")
        font1 = self.fontsMap[fontSource1.getItem()]
        font2 = self.fontsMap[fontSource2.getItem()]
        
        glyphName = self.w.getItem("glyphName").get()
        
        glyph = None
        if glyphName in font1 and glyphName in font2:
            try:
                glyph = RGlyph()
                glyph.interpolate(factor, font1[glyphName], font2[glyphName])                
            except Exception as e:
                print(e)
        
        print(glyph, font1, font2)
        glyphPreview = self.w.getItem("glyphPreview")
        glyphPreview.setGlyph(glyph)
            


Controller()    
