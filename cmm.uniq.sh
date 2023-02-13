cut -d, -f3 bquxjob_44fa60d9_1863e2d2552.csv |awk -F / '{print $NF}' | sort -u | uniq > cmm.out
