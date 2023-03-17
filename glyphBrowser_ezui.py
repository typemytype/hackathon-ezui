import ezui


class EZGlyphBrowserController(ezui.WindowController):

    def build(self):
        content = """
        [__]                 @inputField              # add an input field

        * HorizontalStack    @bottomStack             # add a horizontal stack container

        > |----|             @unicodeCategoryTable    # add a table (in the horizontal stack)

        > ---                                         # add a line (in the horizontal stack)

        > |----|             @unicodeBlockTable       # add a table (in the horizontal stack)

        > * VerticalStack    @outputStack             # add vertical stack (in the horizontal stack)
        >> [_ ?]             @searchField             # add search field (in the vertical stack)
        >> [[__]]            @glyphNamesEditor        # add text editor (in the vertical stack)
        >> (To Spacecenter)  @toSpacecenterButton     # add button (in the vertical stack)
        >> (Lookup)          @lookupButton            # add button (in the vertical stack)
        >> (Add To Font)     @addToFontButton         # add button (in the vertical stack)
        """
        tableHeight = 400
        descriptionData = dict(
            inputTextField=dict(
                height=100,              # set a new height for the input field
            ),

            bottomStack=dict(
                spacing=5                # set spacing for the bottom stack
            ),

            unicodeCategoryTable=dict(
                width=325,               # set the table width
                height=tableHeight       # set the table height
            ),
            unicodeBlockTable=dict(
                width=700,               # set the table width
                height=tableHeight       # set the table height
            ),

            outputStack=dict(
                width=175,                # set the width of the stack
                height=tableHeight,       # set the height of the stack
                distribution="gravity"
            ),
            glyphNamesEditor=dict(
                fontDescription=dict(name="system-monospaced")   # select a font for the text editor
            ),
            toSpacecenterButton=dict(
                width="fill",               # set width to fill the container
                gravity="bottom"            # set gravity to bottom of the container
            ),
            lookupButton=dict(
                width="fill",               # set width to fill the container
                gravity="bottom"            # set gravity to bottom of the container
            ),
            addToFontButton=dict(
                width="fill",               # set width to fill the container
                gravity="bottom"            # set gravity to bottom of the container
            ),
        )
        self.w = ezui.EZWindow(
            content=content,
            descriptionData=descriptionData,
            controller=self,
        )
        inputField = self.w.getItem("inputField")
        inputField.setFont(name="system", size=50)

    def started(self):
        self.w.open()

EZGlyphBrowserController()