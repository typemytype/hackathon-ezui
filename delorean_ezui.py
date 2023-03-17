import ezui


class Controller(ezui.WindowController):

    def build(self):
        # collect all open fonts with and map them to their <familyName> <styleName>
        self.fontsMap = dict()
        for font in AllFonts():
            name = f"{font.info.familyName} {font.info.styleName}"
            if name in self.fontsMap:
                print(f"Duplicated font: {name}")
            self.fontsMap[name] = font

        if not self.fontsMap:
            print("Open some fonts!!!")

        content = """
        * HorizontalStack                                   # add a horizontal stack container
            > ( ...)                    @fontSource1        # add a pop up button (in the horizontal stack)
            > ( ...)                    @fontSource2        # add a pop up button (in the horizontal stack)

        * HorizontalStack                                   # add a horizontal stack container
            > Glyph Name:                                   # add a label (in the horizontal stack)
            > [_       _]               @glyphName          # add an in put field (in the horizontal stack)

        * HorizontalStack                                   # add a horizontal stack container
            > Interpolation:                                # add a label (in the horizontal stack)
            > ---X--- [__]              @interpolation      # add a slider (in the horizontal stack)

        * Box                           @glyphPreviewBox    # add a box contianer
            > * RoboFontGlyphPreview    @glyphPreview       # add RoboFont view: GlyphPreview (in the horizontal stack)

        ===                                                 # start of the footer
        ( ⬇ )                          @generateGlyph       # add a button
        """
        glyph = CurrentGlyph()

        currentGlyphName = ""
        if glyph is not None:
            currentGlyphName = glyph.name

        descriptionData = dict(
            fontSource1=dict(
                items=self.fontsMap.keys()     # fill the pop up button with all open font names
            ),
            fontSource2=dict(
                items=self.fontsMap.keys()     # fill the pop up button with all open font names
            ),
            glyphName=dict(
                width="fill",                  # set width to fill the container
                value=currentGlyphName         # fill the input field with the current glyph name
            ),
            interpolation=dict(
                value=0,                       # set the slider value
                minValue=-200,                 # set the slider minimum value
                maxValue=400,                  # set the slider maximum value
            ),
            glyphPreview=dict(
                height="fill",                 # set height to fill the container
                width="fill",                  # set width to fill the container
                glyph=glyph                    # set a glyph in the GlyphPreview
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
        # get the factor from the slider
        factor = sender.get() / 100

        # get the first source
        fontSource1 = self.w.getItem("fontSource1")
        # get the seconcd source
        fontSource2 = self.w.getItem("fontSource2")
        # get the fonts
        font1 = self.fontsMap[fontSource1.getItem()]
        font2 = self.fontsMap[fontSource2.getItem()]
        # get the glyph name
        glyphName = self.w.getItem("glyphName").get()
        # do nothing when the glyphname is not available in one of the sources
        glyph = None
        if glyphName in font1 and glyphName in font2:
            try:
                # create a new glyph
                glyph = RGlyph()
                # interpolate
                glyph.interpolate(factor, font1[glyphName], font2[glyphName])
            except Exception as e:
                print(e)
        # get the glyph preview
        glyphPreview = self.w.getItem("glyphPreview")
        # set the glyph (interoplated or None when it failed)
        glyphPreview.setGlyph(glyph)


Controller()
