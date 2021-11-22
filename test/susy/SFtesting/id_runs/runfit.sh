

#echo "running goldmini_ID_MC.py"
#cmsRun goldmini_ID_MC.py
#echo "finished goldmini MC"

#echo "running goldmini_ID_MC_finebin.py"
#cmsRun goldmini_ID_MC_finebin.py
#echo "finished goldmini MC fine"


#echo "running goldmini_ID_data.py"
#cmsRun goldmini_ID_data.py
#echo "finished goldmini data"

#echo "running goldmini_ID_data_finebin.py"
#cmsRun goldmini_ID_data_finebin.py
#echo "finished goldmini data fine"




#echo "running medsip data with sipcut"
#cmsRun medsip_ID_Data_sipcut.py
#echo "finished running medsip data with sipcut"

#echo "running mini data with sipcut"
#cmsRun mini_ID_Data_sipcut.py
#echo "finished running mini data with sipcut"

#echo "running medsip mc with sipcut"
#cmsRun medsip_ID_MC_sipcut.py
#echo "finished running medsip mc with sipcut"

#echo "running mini mc with sipcut"
#cmsRun mini_ID_MC_sipcut.py
#echo "finished running mini MC with sipcut"



echo "running medsip data with sip>1"
cmsRun medsip_ID_Data_sipgeq1.py
echo "running medsip data with sip>1"

echo "running medsip mc with sip>1"
cmsRun medsip_ID_MC_sipgeq1.py
echo "running medsip mc with sip>1"

echo "running mini data with sip>1"
cmsRun mini_ID_Data_sipgeq1.py
echo "running mini data with sip>1"

echo "running mini mc with sip>1"
cmsRun mini_ID_MC_sipgeq1.py
echo "running mini mc with sip>1"



