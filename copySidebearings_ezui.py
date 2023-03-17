import ezui


class CopySidebearingsController(ezui.WindowController):

    def build(self):

        # create a list of all open fonts <familyName> <styleName>
        fontNames = [f"{font.info.familyName} {font.info.styleName}" for font in AllFonts()]

        if len(fontNames) < 2:
            print("Open at least 2 fonts!")

        content = """
        Source UFO:                                                         # add a label
        ( ...)                                 @sourceUFOs                  # add a pop up button
        Destination UFO:                                                    # add a label
        ( ...)                                 @destinationUFOs             # add a pop up button
        ----                                                                # add a line
        (X) 􀦳 All Glyphs                      @selectionRadioGroup         # add a radio button with an SF Symbols unicode
        ( ) 􀦷 Selected Glyphs                                              # add a radio button
        ----                                                                # add a line
        ( Copy Sidebearings)                   @copySidebearings            # add a button
        !* open output window for results.                                  # add footnote label
        """
        descriptionData = dict(
            sourceUFOs=dict(
                width="fill",      # set width to fill the container
                items=fontNames    # fill the pop up button with all open font names
            ),
            destinationUFOs=dict(
                width="fill",      # set width to fill the container
                items=fontNames,   # fill the pop up button with all open font names
                selected=1
            ),
            copySidebearings=dict(
                width="fill"       # set width to fill the container
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
