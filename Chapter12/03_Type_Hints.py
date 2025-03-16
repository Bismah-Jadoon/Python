from typing import List, Tuple, Dict, Union

a : List[int] = [1,2,3,4]
b : Tuple[str,int] = ("Alice", 24)
c : Dict[str,int] = {"Alice":24, "Bob":20}
d : Union[int,str] = "ID123"


print(a,b,c,d)