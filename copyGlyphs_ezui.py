import ezui

class CopyGlyphsController(ezui.WindowController):

    def build(self):        
        self.fontsMap = dict()
        glyphOrder = None
        for font in AllFonts():
            if glyphOrder is None:
               glyphOrder = font.glyphOrder 
            name = f"{font.info.familyName} {font.info.styleName}"
            if name in self.fontsMap:
                print(f"Duplicated font: {name}")
            self.fontsMap[name] = font
        
        if not self.fontsMap:
            print("Open some fonts!!!")
                    
        content = """
        = HorizontalStack
            * VerticalStack
            > Source Font:
            > ( ...)                     @fonts        
            > | |                        @glyphsList
            
            * VerticalStack
            > Destination Fonts:
            > | |                        @destinationFontsList
            > [X] Ovewrite glyphs
            > [ ] Mark Glyphs
        
        =========
        
        * VerticalStack              @footer
        > ---------------
        > ( Copy Glyphs )            @copyGlyphsButton
        """
        descriptionData = dict(
            fonts=dict(
                width="fill",
                items=self.fontsMap.keys()
            ),
            destinationFontsList=dict(
                items=list(self.fontsMap.keys())[1:]
            ),    
            glyphsList=dict(
                width="fill",                
                items=glyphOrder
            ),
            copyGlyphsButton=dict(),
            footer=dict(
                alignment="trailing"
            )
        )
        self.w = ezui.EZWindow(
            title="Copy Glyphs",
            content=content,
            descriptionData=descriptionData,
            size=(500, 300),
            minSize=(500, 300),            
            controller=self
        )
    
    def started(self):
        self.w.open()
    
    def fontsCallback(self, sender):
        items = sender.getItems()
        fontName = items[sender.get()]
        font = self.fontsMap[fontName]
        
        destinationFontsList = self.w.getItem("destinationFontsList")
        destinationFontsList.set([name for name in items if name != fontName])

        glyphsList = self.w.getItem("glyphsList")
        glyphsList.set(font.glyphOrder)
    
    def copyGlyphsButtonCallback(self, sender):
        print("Copy Glyphs!!")
        


CopyGlyphsController()    

