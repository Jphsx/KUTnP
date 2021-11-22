#original reweighting
#root -l -b -q /home/t3-ku/janguian/HADD/tempstorage/TnP_ZmumuM502017_100File.root /home/t3-ku/janguian/HADD/tempstorage/TnP_SingleMuon2017C_zmumu_1.root addNVtxWeight.cxx++



#reweighting for boosted MC with more files, used for finer binning on SF
root -l -b -q /home/t3-ku/janguian/HADD/tempstorage/TnP_ZmumuM502017_200File.root /home/t3-ku/janguian/HADD/tempstorage/TnP_SingleMuon2017C_zmumu_1.root addNVtxWeight.cxx++
