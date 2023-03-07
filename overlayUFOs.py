import os
import ezui


class Controller(ezui.WindowController):

    def build(self):
        content = """
        = HorizontalStack
        * VerticalStack
            > [X] Show
            > [X] Fill
            > * ColorWell                    @layerColor
            > [ ] Stroke
            > ---
            > Alignment:
            > (X) Left
            > ( ) Center
            > ( ) Right
        * VerticalStack
            > |---|                           @fontList    
            > (+-)                            @fontListAddRemoveButton
            > ---
            > * HorizontalStack
                >> Contexts:
                >> [ ] Always View Current
            > * HorizontalStack
                >> [_ _]                       @leftContext
                >> [_ _]                       @glyphContext
                >> [_ _]                       @rightContext
        """
        descriptionData = dict(
            layerColor=dict(
                width=70,
                color=(1, 0, 0, .4)
            ),
            fontList=dict(
                width="fill",
                columnDescriptions=[
                    dict(title="􀋭", identifier="show", cellDescription=dict(cellType="Checkbox"), width=20, editable=True),
                    dict(title="Path", identifier="path"),
                ]
            ),
            leftContext=dict(
                width=100,
                placeholder="Left Context"
            ),
            glyphContext=dict(
                width=60
            ),
            rightContext=dict(
                width=100,
                placeholder="Right Context"
            ),            
        )
        self.w = ezui.EZPanel(
            title="Overlay UFOs",
            content=content,
            descriptionData=descriptionData,
            size=(500, 400),
            controller=self
        )
    
    def started(self):
        self.w.open()
    
    def fontListAddRemoveButtonAddCallback(self, sender):
        
        def showGetFileResultCallback(result):
            print(result)
            if result is None:
                return
            
            table = self.w.getItem("fontList")
            items = table.get()

            for path in result:
                item = table.makeItem(
                    show=True,
                    path=os.path.basename(path),
                    fullPath=path
                )
                items.append(item)
                
            table.set(items)
        
        self.showGetFile(
            messageText="Select a ufo.",
            fileTypes=["ufo"],
            allowsMultipleSelection=True,            
            callback=showGetFileResultCallback
        )
        

    def fontListAddRemoveButtonRemoveCallback(self, sender):
        table = self.w.getItem("fontList")
        selection = table.getSelectedIndexes()
        items = table.get()
        for index in reversed(sorted(selection)):
            del items[index]
        table.set(items)


Controller()    
