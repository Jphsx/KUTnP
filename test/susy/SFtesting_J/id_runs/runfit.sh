

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






#echo "running med data"
#cmsRun med_ID_Data.py
#echo "finished med data"


#echo "running sip data"
#cmsRun sip_ID_Data.py
#echo "finished sip data"


#echo "running medsip data"
#cmsRun medsip_ID_Data.py
#echo "finished medsip data"




#echo "running med mc"
#cmsRun med_ID_MC.py
#echo "finished med mc"


#echo "running sip mc"
#cmsRun sip_ID_MC.py
#echo "finished sip mc"

#echo "running medsip mc"
#cmsRun medsip_ID_MC.py
#echo "finished medsip mc"


echo "running medsip no trig data"
cmsRun medsip_noTrig_ID_Data.py
echo "finished medsip no trig data"

echo "running medsip no trig mc"
cmsRun medsip_noTrig_ID_MC.py
echo "finished medsip no trig mc"
