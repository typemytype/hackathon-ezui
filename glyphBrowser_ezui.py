import ezui

class EZGlyphBrowserController(ezui.WindowController):

    def build(self):
        content = """
        [__]                 @inputField

        * HorizontalStack    @bottomStack

        > |----|             @unicodeCategoryTable

        > ---

        > |----|             @unicodeBlockTable

        > * VerticalStack    @outputStack
        >> [_ ?]             @searchField
        >> [[__]]            @glyphNamesEditor
        >> (To Spacecenter)  @toSpacecenterButton
        >> (Lookup)          @lookupButton
        >> (Add To Font)     @addToFontButton
        """
        tableHeight = 400
        descriptionData = dict(
            inputTextField=dict(
                height=100,     
            ),

            bottomStack=dict(
                spacing=5
            ),

            unicodeCategoryTable=dict(
                width=325,
                height=tableHeight
            ),
            unicodeBlockTable=dict(
                width=700,
                height=tableHeight
            ),
            
            outputStack=dict(
                width=175,
                height=tableHeight,
                distribution="gravity"
            ),
            glyphNamesEditor=dict(
                fontDescription=dict(name="system-monospaced")
            ),            
            toSpacecenterButton=dict(
                width="fill",
                gravity="bottom"
            ),
            lookupButton=dict(
                width="fill",
                gravity="bottom"
            ),
            addToFontButton=dict(
                width="fill",
                gravity="bottom"
            ),
        )
        self.w = ezui.EZWindow(
            content=content,
            descriptionData=descriptionData,
            controller=self,
            # minSize=(500, 300),
            # size=(1000, 500)
        )
        inputField = self.w.getItem("inputField")
        inputField.setFont(name="system", size=50)
        
    def started(self):
        self.w.open()

EZGlyphBrowserController()