import ezui

class LetterMeterController(ezui.WindowController):

    def build(self):
        content = """
        = VerticalSplits 
        * SplitsPane  @inputPane
        > [[_ _]]     @inputText
        
        * SplitsPane  @output_1_pane  
        > [[_ _]]     @output_1

        * SplitsPane  @output_2_pane
        > [[_ _]]     @output_2
        
        * SplitsPane  @output_3_pane
        > [[_ _]]     @output_3

        
        =======
        * HorizontalStack
        ( Analyze )   @analyzeButton
        [X] Ignore case
        """
        descriptionData = dict(            
            inputPane=dict(
                preferredThickness=300,
                minThickness=50,
                priority=80,                
            ),
            output_1_pane=dict(
                minThickness=150,
                maxThickness=200,
                priority=90
            ),
            output_2_pane=dict(
                minThickness=150,
                maxThickness=200,
                priority=100
            ),
            output_3_pane=dict(
                minThickness=150,
                maxThickness=200,
                priority=90
            ),
            inputText=dict(
                height="fill",
                value="Als Gregor Samsa eines Morgens aus unruhigen Träumen erwachte, fand ersich in seinem Bett zu einem ungeheuren Ungeziefer verwandelt. Er lagauf seinem panzerartig harten Rücken und sah, wenn er den Kopf ein wenighob, seinen gewölbten, braunen, von bogenförmigen Versteifungengeteilten Bauch, auf dessen Höhe sich die Bettdecke, zum gänzlichenNiedergleiten bereit, kaum noch erhalten konnte. Seine vielen, imVergleich zu seinem sonstigen Umfang kläglich dünnen Beine flimmertenihm hilflos vor den Augen."                
            ),
            output_1=dict(
                height="fill",
                editable=False,
                fontDescription=dict(name="system-monospaced")
            ),
            output_2=dict(
                height="fill",
                editable=False,
                fontDescription=dict(name="system-monospaced")
            ),
            output_3=dict(
                height="fill",
                editable=False,
                fontDescription=dict(name="system-monospaced")
            ),
        )
        self.w = ezui.EZWindow(
            title="Letter Frequency Meter",
            content=content,
            descriptionData=descriptionData,
            size=(800, 500),
            minSize=(600, 400),
            controller=self,
        )
    
    def started(self):
        self.w.open()
    
    def inputTextCallback(self, sender):
        output_1 = self.w.getItem("output_1")
        output_1.set("hello world")
        
        output_2 = self.w.getItem("output_2")
        output_2.set("100\n123")
        
        output_3 = self.w.getItem("output_3")     
        output_3.set("---\nfoo\n---\nbar\n---")
           
        print("Update output columns.")
        print(sender.get())
    
    def analyzeButton(self, sender):
        inputText = self.w.getItem("inputText")
        print("analyze the text")
        print(inputText.get())


LetterMeterController()    
