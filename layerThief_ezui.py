import ezui
import ezui
import drawBot
import functools


@functools.cache
def colorImage(color, width=20, height=12):
    if color is None:
        return None
    drawBot.newDrawing()
    drawBot.newPage(width, height)    
    drawBot.fill(*color)    
    drawBot.rect(0, 0, width, height)    
    im = drawBot.saveImage("NSImage")
    drawBot.endDrawing()
    return im


class LayerThiefController(ezui.WindowController):

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
        = TwoColumnForm
        : Source: 
        (( ...))                             @sourceFont
        (( ...))                             @sourceLayer
        ---
        
        : Target:
        (( ...))                             @targetFont
        (( ...))                             @targetLayer
        ---
        
        [X] Overwrite Target Layer Glyphs    @overwriteTarget
        [ ] Include Marks                    @includeMarks
        
        =====        
        ( Copy )                             @copyButton
        """
        descriptionData = dict(
            content=dict(
                itemColumnWidth=300
            ),
            sourceFont=dict(
                width="fill",                               
            ),
            targetFont=dict(
                width="fill"
            ),
            sourceLayer=dict(
                width="fill"                
            ),
            targetLayer=dict(
                width="fill",
            ),
            overwriteTarget=dict(
                sizeStyle="small"
            ),
            includeMarks=dict(
                sizeStyle="small"
            ),
        )
        
        self.w = ezui.EZWindow(
            title="Layer Thief",
            content=content,
            descriptionData=descriptionData,
            size=(300, "auto"),
            controller=self
        )
        
        self.setFontData()
    
    def started(self):
        self.w.open()
    
    def setFontData(self):
        sourceFont = self.w.getItem("sourceFont")
        sourceFont.setItemDescriptions([dict(text=fontName, callback=self.sourceFontChangedCallback) for fontName in self.fontsMap])        
        
        targetFont = self.w.getItem("targetFont")
        targetFont.setItemDescriptions(
            [dict(text=fontName, callback=self.targetFontChangedCallback) for fontName in self.fontsMap] +
            [
                "---",
                dict(text="Open Font...", callback=self.openTargetFontCallback)
            ]
        )
        self.setLayerData()
    
    def setLayerData(self):
        sourceFont = self.w.getItem("sourceFont")
        font = self.fontsMap[sourceFont.getItem()]
        
        sourceLayer = self.w.getItem("sourceLayer")
        sourceLayer.setItemDescriptions(
            [dict(image=colorImage(layer.color), text=layer.name) for layer in font.layers]
        )
        
        targetFont = self.w.getItem("targetFont")
        font = self.fontsMap[targetFont.getItem()]
        
        targetLayer = self.w.getItem("targetLayer")
        targetLayer.setItemDescriptions(
            [dict(image=colorImage(layer.color), text=layer.name) for layer in font.layers] +
            [
                "---",
                dict(text="Add Layer...", callback=self.addTargetLayerCallback)
            ]
        )                
    
    # notifications
    
    def copyButtonCallback(self, sender):
        print(self.w.content.getItems())
    
    def sourceFontChangedCallback(self, sender):
        print("set source layer data")
        self.setLayerData()
    
    def targetFontChangedCallback(self, sender):
        print("set target layer data")
        self.setLayerData()
        
    # menu
    
    def openTargetFontCallback(self, sender):
        print("open Target Font and select it!")
        self.w.getItem("targetFont").set(0)
    
    def addTargetLayerCallback(self, sender):
        print("add layer in target")
        
LayerThiefController()    
