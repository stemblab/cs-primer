resources

diaryinit('Aw_cob-1.txt')
diary on; 
disp(acc_dump_matrix(3,12,1)); %. $W_1$
diary off 

diaryinit('Aw_cob-2.txt')
diary on
Aw=[acc_dump_matrix(3,12,1);
    acc_dump_matrix(3,12,2);
    acc_dump_matrix(3,12,3);
    acc_dump_matrix(3,12,4)]
diary off

