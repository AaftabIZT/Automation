from framework.Libraries_Pkg.Func import *
from framework.config import *


url = base_url+instance_id+"/snapshots"

snapshots=get_exhistingsnapshotList(url)

print snapshots