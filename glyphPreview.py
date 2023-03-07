import ezui

class Controller(ezui.WindowController):

    def build(self):
        content = """
        * RoboFontGlyphPreview  @glyphPreview
        """
        descriptionData = dict(
            glyphPreview=dict(
                height="fill",
                glyph=CurrentGlyph(),
                selection=[(100, 100)]
            )
        )
        self.w = ezui.EZWindow(
            content=content,
            descriptionData=descriptionData,
            title="Title",
            size=(400, 400),
            controller=self
        )
        
        #self.w.getItem("glyphPreview").setGlyph(CurrentGlyph())
    
    def started(self):
        self.w.open()


Controller()    
