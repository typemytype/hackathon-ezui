import ezui
import drawBot
import functools



@functools.cache
def colorImage(color, width=20, height=12):
    """
    A helper function to create an nsImage object with a color
    with a given width and height
    This requires drawBot to be installed
    """
    if color is None:
        return None
    # start a new drawing
    drawBot.newDrawing()
    # set the width and height
    drawBot.newPage(width, height)
    # set the fill color
    drawBot.fill(*color)
    # draw a rectangle
    drawBot.rect(0, 0, width, height)
    # get the nsImage object from drawBot
    im = drawBot.saveImage("NSImage")
    # end the drawing
    drawBot.endDrawing()
    # retutn the nsImage object
    return im


class LayerThiefAddLayerController(ezui.WindowController):

    def build(self, parent, callback):
        self.callback = callback

        content = """
        = TwoColumnForm                    # switch to a 2 column form
        : Color:                           # add form label
        * ColorWell      @layerColor       # add a colorwell

        : Name:                            # add form label
        [_       _]      @layerName        # add a text field

        ====                               # start a footer
        ( Cancel )       @cancelButton     # add a button
        ( Add Layer )    @addlayerButton   # add a button
        """
        descriptionData = dict(
            content=dict(
                itemColumnWidth=150       # set the width of the item columns of the two column form
            ),
            layerColor=dict(
                height=20,                # set height of the colorwell
                color=(1, 0, 1, 1)        # set color of the colorwell
            ),
            layerName=dict(
                placeholder="Layer name"  # set a placeholder text in the text field
            )
        )
        self.w = ezui.EZSheet(   # open the in a sheet with a parent window
            content=content,
            descriptionData=descriptionData,
            parent=parent,
            size=(200, "auto"),
            controller=self
        )

    def started(self):
        self.w.open()

    def cancelButtonCallback(self, sender):
        self.w.close()

    def addlayerButtonCallback(self, sender):
        layerName = self.w.getItem("layerName")
        layerColor = self.w.getItem("layerColor")
        self.callback(layerName.get(), layerColor.get())
        self.w.close()


class LayerThiefController(ezui.WindowController):

    def build(self):
        # collect all open fonts with and map them to their <familyName> <styleName>
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
        = TwoColumnForm                                             # switch to a 2 column form
        : Source:                                                   # add form label
        (( ...))                             @sourceFont            # add pull down button
        (( ...))                             @sourceLayer           # add pull down button
        ---                                                         # add a line

        : Target:                                                   # add form label
        (( ...))                             @targetFont            # add pull down button
        (( ...))                             @targetLayer           # add pull down button
        ---                                                         # add a line

        [X] Overwrite Target Layer Glyphs    @overwriteTarget       # add a checkbox
        [ ] Include Marks                    @includeMarks          # add a checkbox

        =====                                                       # start a footer
        ( Copy )                             @copyButton            # add a button
        """
        descriptionData = dict(
            content=dict(
                itemColumnWidth=300           # set the width of the item columns of the two column form
            ),
            sourceFont=dict(
                width="fill",                 # set width to fill the container
            ),
            targetFont=dict(
                width="fill"                  # set width to fill the container
            ),
            sourceLayer=dict(
                width="fill"                  # set width to fill the container
            ),
            targetLayer=dict(
                width="fill",                 # set width to fill the container
            ),
            overwriteTarget=dict(
                sizeStyle="small"             # set vanilla sizeStyle to small
            ),
            includeMarks=dict(
                sizeStyle="small"             # set vanilla sizeStyle to small
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
        # get the source pull down button
        sourceFont = self.w.getItem("sourceFont")
        # set all fonts names in the menu
        sourceFont.setItemDescriptions([dict(text=fontName, callback=self.sourceFontChangedCallback) for fontName in self.fontsMap])
        # get the target pull down button
        targetFont = self.w.getItem("targetFont")
        # set all fonts names in the menu + add a "Open Font..."
        targetFont.setItemDescriptions(
            [dict(text=fontName, callback=self.targetFontChangedCallback) for fontName in self.fontsMap] +
            [
                "---",
                dict(text="Open Font...", callback=self.openTargetFontCallback)
            ]
        )
        self.setLayerData()

    def setLayerData(self):
        # get the source pull down button
        sourceFont = self.w.getItem("sourceFont")
        # get the font
        font = self.fontsMap[sourceFont.getItem()]
        # get the source layers pull down button
        sourceLayer = self.w.getItem("sourceLayer")
        # set all layer from the selected font with color images
        sourceLayer.setItemDescriptions(
            [dict(image=colorImage(layer.color), text=layer.name) for layer in font.layers]
        )
        # get the target pull down button
        targetFont = self.w.getItem("targetFont")
        # get the font
        font = self.fontsMap[targetFont.getItem()]
        # get the target layers pull down button
        targetLayer = self.w.getItem("targetLayer")
        # set all layer from the selected font with color images
        # + add a "Addn Layer..." option
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
        LayerThiefAddLayerController(self.w, self._addTargetLayer)

    def _addTargetLayer(self, layerName, layerColor):
        targetFont = self.w.getItem("targetFont")
        font = self.fontsMap[targetFont.getItem()]
        print(f"add layer '{layerName}' color: {layerColor} in {font}")
        targetLayer = self.w.getItem("targetLayer")
        # select the newly added layer
        targetLayer.set(2)



LayerThiefController()
