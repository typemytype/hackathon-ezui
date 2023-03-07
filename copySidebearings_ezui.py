import ezui

class CopySidebearingsController(ezui.WindowController):

    def build(self):
        
        fontNames = [f"{font.info.familyName} {font.info.styleName}" for font in AllFonts()]
        
        if len(fontNames) < 2:
            print("Open at least 2 fonts!")
            
        content = """
        Source UFO:
        ( ...)                                 @sourceUFOs
        Destination UFO:
        ( ...)                                 @destinationUFOs
        ----
        (X) 􀦳 All Glyphs                      @selectionRadioGroup
        ( ) 􀦷 Selected Glyphs
        ----
        ( Copy Sidebearings)                   @copySidebearings
        !* open output window for results.
        """
        descriptionData = dict(
            sourceUFOs=dict(
                width="fill",
                items=fontNames
            ),
            destinationUFOs=dict(
                width="fill",
                items=fontNames,
                selected=1
            ),
            copySidebearings=dict(
                width="fill"
            )
        )
        self.w = ezui.EZPanel(
            content=content,
            descriptionData=descriptionData,
            title="CopySidebearings",
            size="auto",
            controller=self
        )
    
    def started(self):
        self.w.open()
    
    def copySidebearingsCallback(self, sender):
        print("Copy Sidebearings")
        selectionRadioGroup = self.w.getItem("selectionRadioGroup")
        print("selection:", selectionRadioGroup.get())
        


CopySidebearingsController()    
