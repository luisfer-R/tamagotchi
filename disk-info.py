from diskinfo import Disk, DiskInfo

Disk_Info = {}

di = DiskInfo()
# get disks
disks = di.get_disk_list(sorting=True)
for d in disks:
    dis = Disk(d.get_path().split('/')[-1])
    plist = dis.get_partition_list()
    Disk_Info[d.get_path().split('/')[-1]] = {"path": d.get_path()}
    Partitions = []
    for p in plist:
        Partitions+=[p.get_name()]
    Disk_Info[d.get_path().split('/')[-1]]["partitions"] = Partitions

print(Disk_Info)

#documents
#https://diskinfo.readthedocs.io/en/latest/intro.html
#https://diskinfo.readthedocs.io/en/latest/api.html
