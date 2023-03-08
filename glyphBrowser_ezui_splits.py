import ezui

class Controller(ezui.WindowController):

    def build(self):
        content = """
        * HorizontalSplits
        > * SplitsPane                 @inputTextPane
            >> [_ _]                   @inputText
        > * SplitsPane
            >> * VerticalSplits
            >>> * SplitsPane           @unicodeCategoryListPane
                >>>> |---|             @unicodeCategoryList
            >>> * SplitsPane           @unicodeBlocksListPane
                >>>> |---|             @unicodeBlocksList
            >>> * SplitsPane           @outputPane        
                >>>> [_ ?]             @search 
                >>>> [[_ _]]           @glyphNames
                >>>> ( Lookup )
                >>>> ( Add To Font )
        """
        descriptionData = dict(
            inputTextPane=dict(
                minThickness=20,
                maxThickness=20,
                preferredThickness=20,
            ),
            inputText=dict(
                width="fill",                
            ),
            unicodeCategoryListPane=dict(
                minThickness=200,
                preferredThickness=300,
                priority=100
            ),
            unicodeBlocksListPane=dict(
                minThickness=100,
                preferredThickness=500,
                priority=80
            ),
            outputPane=dict(
                minThickness=100,
                preferredThickness=500,
                priority=110,
            ),

            unicodeCategoryList=dict(),
            unicodeBlocksList=dict(),            
        )
        self.w = ezui.EZWindow(
            title="Glypyh Browser",
            content=content,
            descriptionData=descriptionData,
            size=(800, 500),
            minSize=(400, 300),
            margins=0,
            controller=self
        )
    
    def started(self):
        self.w.open()


Controller()    
