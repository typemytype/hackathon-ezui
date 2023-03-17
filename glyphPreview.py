import ezui

class Controller(ezui.WindowController):

    def build(self):
        content = """
        * RoboFontGlyphPreview  @glyphPreview          # add custom RF view
        """
        descriptionData = dict(
            glyphPreview=dict(
                height="fill",              # set height to fill the container
                glyph=CurrentGlyph(),       # set glyph
                selection=[(100, 100)]      # set point to hightlight
            )
        )
        self.w = ezui.EZWindow(
            content=content,
            descriptionData=descriptionData,
            title="Title",
            size=(400, 400),
            controller=self
        )

    def started(self):
        self.w.open()


Controller()
