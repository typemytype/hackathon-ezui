import ezui


class CopyGlyphsController(ezui.WindowController):

    def build(self):
        # collect all open fonts with and map them to their <familyName> <styleName>
        self.fontsMap = dict()
        glyphOrder = []
        for font in AllFonts():
            if not glyphOrder:
               glyphOrder = font.glyphOrder
            name = f"{font.info.familyName} {font.info.styleName}"
            if name in self.fontsMap:
                print(f"Duplicated font: {name}")
            self.fontsMap[name] = font

        if not self.fontsMap:
            print("Open some fonts!!!")

        content = """
        = HorizontalStack                                              # switch from the default vertical stack to a horizontal stack
            * VerticalStack                                            # add a vertical stack container
            > Source Font:                                             # add a label
            > ( ...)                     @fonts                        # add a pop up button with identifier
            > |---|                      @glyphsList                   # add a table with identifier

            * VerticalStack                                            # add a vertical stack container
            > Destination Fonts:                                       # add a label
            > |---|                      @destinationFontsList         # add a table with identifier
            > [X] Ovewrite glyphs                                      # add a checkbox and mark it
            > [ ] Mark Glyphs                                          # add a checkbox

        =----=                                                         # start of the footer with a line above

        ( Copy Glyphs )            @copyGlyphsButton                   # add button with identifier
        """
        descriptionData = dict(
            fonts=dict(
                width="fill",                 # set width to fill the container
                items=self.fontsMap.keys()    # fill the pop up button with all open font names
            ),
            destinationFontsList=dict(
                items=list(self.fontsMap.keys())[1:]        # fill the table with a all open fonts except the active on in the pop up button
            ),
            glyphsList=dict(
                width="fill",               # set width to fill the container
                items=glyphOrder            # fill the table with glypsh from the active font in the pop up button
            ),
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

