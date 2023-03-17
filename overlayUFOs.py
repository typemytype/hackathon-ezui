import os
import ezui


class Controller(ezui.WindowController):

    def build(self):
        content = """
        = HorizontalStack                                                           # switch from the default vertical stack to a horizontal stack
        * VerticalStack                                                             # add a vertical stack
            > [X] Show                                                              # add check box (in vertical stack)
            > [X] Fill                                                              # add check box (in vertical stack)
            > * ColorWell                    @layerColor                            # add color well (in vertical stack)
            > [ ] Stroke                                                            # add check box (in vertical stack)
            > ---                                                                   # add line (in vertical stack)
            > Alignment:                                                            # add label (in vertical stack)
            > (X) Left                                                              # add radio button (in vertical stack)
            > ( ) Center                                                            # add radio button (in vertical stack)
            > ( ) Right                                                             # add radio button (in vertical stack)

        * VerticalStack                                                             # add a vertical stack
            > |---|                           @fontList                             # add table (in vertical stack)
            > (+-)                            @fontListAddRemoveButton              # add +- segmented button (in vertical stack)
            > ---                                                                   # add line (in vertical stack)
            > * HorizontalStack                                                     # add a horizontal stack (in vertical stack)
                >> Contexts:                                                        # add label (in horizontal stack)
                >> [ ] Always View Current                                          # add checkbox (in horizontal stack)
            > * HorizontalStack                                                     # add a horizontal stack (in vertical stack)
                >> [_ _]                       @leftContext                         # add text field (in horizontal stack)
                >> [_ _]                       @glyphContext                        # add text field (in horizontal stack)
                >> [_ _]                       @rightContext                        # add text field (in horizontal stack)
        """
        descriptionData = dict(
            layerColor=dict(
                width=70,
                color=(1, 0, 0, .4)
            ),
            fontList=dict(
                width="fill",
                columnDescriptions=[
                    # add column with a checkbox as cell type
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
