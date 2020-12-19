"""Parser Module."""
from time import time
a = time()

import __init__
from Parser.collect import *

class Parser:
    """Parser Class."""

    _objId:str = "id"
    _refObj:str = "reference"
    _constr:str = "construct"
    _paramLst:str = "parameterList"

    _new:str = "new"

    _type:str = "type"
    _desc:str = "description"
    _val:str = "value"

    _idLexicon:str = "^[A-Za-z_]\\w*$"
    def __init__(self) -> None:
        """Construct default configuration. Initializes components."""
        super().__init__()
        self.rules = Collector().getDS()
        self.symtab = {}

    @staticmethod
    def parse(arg):
        if "-h" == arg:
            pass
        

    def inputTokenizer(self, fileName:str):
        """Read in file and tokenizes it."""
        with open(fileName) as file:
            fileContent = file.read()
        line = 0
        fileContent = fileContent.split("\n")
        for content in fileContent:
            line += 1
            content = content.split()
            try:
                content = {
                    self._objId:content[0],
                    self._refObj:content[1],
                    self._constr:content[2],
                    self._paramLst:content[3:]
                }
            except:
                l = len(content)
                if l == 0:
                    print(
                        f"Line {line}. \tEmpty"
                    )
                    continue
                else:
                    print(
                        f"Line {line}. \tSyntaxError:",
                        f"\tExpected atleast 3 tokens, received {l}"
                    )
                continue
            yield (line, content)

    def processConstruction(self, _ref:str, _constr:str, _id:str, _param:list):
        """Deals with construction per instruction."""
        if _ref == self._new:
            try:
                obj = objectADT[_constr]
            except:
                raise Exception(
                    f"TypeError:\tExpected a subclass of Drawable,"+
                    f" received {_constr}"
                )
            if issubclass(obj, initOrder):
                return self.newConstruction(_constr, self.rules[obj][self._new],_id, _param)
            raise Exception(
                f"TypeError:\tExpected a subclass of Drawable,"+
                f" received {obj.__name__}"
            )
        try:
            obj = self.symtab[_ref]
        except:
            raise Exception(
                f"ValueError:\tObject {_ref} not declared before."
            )
        tp, obj = obj[self._type], obj[self._val]
        if issubclass(tp, initOrder):
            try:
                methodDict:dict = self.rules[tp][_constr]
            except:
                raise Exception(
                    f"OpsError:\tOperation {tp.__name__}->{_constr} not available."
                )
            return self.objectConstruction(obj, _constr, methodDict, _id, _ref, _param)
        raise Exception(
            f"TypeError:\tExpected a subclass of Drawable,"+
            f" received {tp.__name__}"
        )

    def resolveParameters(self, paramList:list, forConstructor:bool=False):
        """Resolve parameters according to types."""
        paramValue = list()
        paramType  = list()
        for item in paramList:
            try:
                val = self.symtab[item][self._val ]
                tp  = self.symtab[item][self._type]
            except:
                try:
                    val = float(item)
                    tp  = float
                except:
                    raise ValueError(
                        f"ValueError:\tValue for {item}"
                        +" couldn't be resolved."
                    )
            paramType.append(tp )
            paramValue.append(val)
        if forConstructor and len(paramList) > 2:
            if   all([x == Point for x in paramType]):
                paramType = (Point,)
                paramValue= (paramValue,)
                return (paramType, paramValue)
            elif all([x == Line  for x in paramType]):
                paramType = (Line,)
                paramValue= (paramValue,)
                return (paramType, paramValue)
        return (tuple(paramType), tuple(paramValue))

    def newConstruction(self, constr:str, constructorDict:dict, _id:str, param):
        """Construct brand 'new' Drawable object."""
        types, values = self.resolveParameters(param, forConstructor=True)
        try:
            target = constructorDict[types]
        except:
            raise ValueError(
                f"ValueError:\tParameter list: {param} of "+
                f"types: {types} doesn't match with any "+
                f"parameter list for construction of {constr}"
            )
        values = dict(zip(target[args], values))
        target = target[trgt]
        types = constructorDict[ret]
        return {
            self._type  :types,
            self._desc  :f"{_id} is {types.__name__} using {target.__name__}"+
                         f" with parameters {param}",
            self._val   :target(**values)
        }

    def objectConstruction(self, ref, constr, methodDict:dict, _id:str, _refid:str, param:list):
        """Construct object from existing Drawable object or perform some computation."""
        types, values = self.resolveParameters(param)
        try:
            target = methodDict[types]
        except:
            raise ValueError(
                f"ValueError:\tParameter list: {param} of "+
                f"types: {types} doesn't match with any "+
                f"parameter list for construction of {constr}"
            )
        values = dict(zip(target[args], values))
        target = target[trgt]
        types = methodDict[ret]
        return {
            self._type  :types,
            self._desc  :f"{_id} is {types.__name__} {target.__name__}"+
                         f" on {_refid} with parameters {param}",
            self._val   :target(ref, **values)
        }

    def tokenChecker(self, fileName:str):
        """Start point of operations."""
        from re import match
        for (line, instruction) in self.inputTokenizer(fileName):
            _id:str = instruction[self._objId]
            if match(self._idLexicon, _id) == None:
                print(
                    f"Line {line}. \tIDError:",
                    "\tIdentifier doesn't follow naming convension."
                )
            if _id in self.symtab:
                print(
                    f"Line {line}. \tObject exists with same id.",
                    "Can't proceed without overwriting.",
                    "Skipping"
                )
                continue
            try:
                self.symtab[_id] = self.processConstruction(
                    instruction[self._refObj  ],
                    instruction[self._constr  ],
                    _id,
                    instruction[self._paramLst]
                )
            except Exception as e:
                print(
                    f"Line {line}. \t",
                    e.args[0]
                )

    def draw(self, _storageName="./data/store.png", _store=True, _show=False):
        """Stage DS to be drawable under Drawable library specification."""
        drawableList = []
        for x in self.symtab.values():
            if issubclass(x[self._type], Drawable):
                drawableList.append(x[self._val])
                continue
            drawableList.append((x[self._desc], x[self._val]))
        figure = Drawable.draw(
            drawables=drawableList, _storageName=_storageName,
            _store=_store, _show=_show
        )
        return (drawableList, figure)

if __name__ == "__main__":
    # a = processConstruction(_new, "point", ["12", "0.9"])
    from sys import argv
    p = Parser()
    p.tokenChecker(argv[1])
    p.draw()
    for item in p.symtab.values():
        print(item[p._desc])


