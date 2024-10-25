from diskinfo import Disk, DiskInfo

di = DiskInfo()
disks = di.get_disk_list(sorting=True)
for d in disks:
    dis = Disk(d.get_path().split('/')[-1])
    plist = dis.get_partition_list()
    print(d.get_path())
    for p in plist:
        print(p.get_name())


#documents
https://diskinfo.readthedocs.io/en/latest/intro.html
https://diskinfo.readthedocs.io/en/latest/api.html
