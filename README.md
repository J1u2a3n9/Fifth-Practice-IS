# FIFTH PRACTICE INTELLIGENT SYSTEMS
# TIC TAC TOE

<p align="center">
  <img src="https://s3.amazonaws.com/s3.timetoast.com/public/uploads/photo/10447262/image/b99e85ef89ddf17c87ad356f4727aaa0" alt="Sublime's custom image"/>
</p>

## NAMES 📋
* Balderrama Mauricio
* Canedo Juan Luis
* La Fuente Mercedes

### IMPORTANT! HOW TO USE :hammer:


## PROBLEM SOLVER AGENT ⚙️

### Objective Formulation:
Implement the intelligent N in dash (3, 4, 5 in dash) also known as tic-tac-toe with the algorithms MinMax, AlphaBeta Prunning and MinMaxCutof.

### Problem Formulation:


### Initial State:
A n*n size board that is empty

### Objective State:
The same board with a number and positioning of x or circles that define a winner or tie.  

### Test of Objective:
Can the program make an intelligent decision of where to put its x or circle so that it always wins or draws?

### Actions:
* Place an x or circle in an available position on the board. 




## DESCRIPTION OF THE PROBLEM
You must generate an intelligent program that allows you to analyze all possible states that are beneficial against a human opponent by implementing algorithms that will make it intelligent such as MinMax, MinMax + AlphaBeta Prunning.
and MinMaxCutOff 


## SOLUTION DESCRIPTION
The program allows to generate a board of dimensions n * n that are greater or equal to three, it also allows to choose if the first player will be human or the same program which has implemented the requested algorithms, the first player is always x whether it is the computer or human and also the program always looks for the best solution so that it wins or draws against its opponent.


## EXPERIMENTS :round_pushpin:

### NOTES
Each experiment performed was done in an environment in which the two agents are the computer and the same algorithm. 

#### 1.Number of expanded states, Execution time and Execution result for board 3x3

#### :arrow_down_small: Experiments and results:

##### Min Max Agent 


  Run Time X (second) |  Run time O (second) |  States Visited X | States Visited O | Winner
  :---: | :---: | :---: | :---: | :---: 
  8.76531162 | 1.423083000006 | 557487 | 60688 | Draw
  7.72937368 | 1.1550937750045 | 1114974 | 121376 | Draw 
  8.19679900 | 1.0290801999992 | 1245897 | 157891 | Draw
  
  
  
 ##### Min Max Alpha Beta Prunning Agent 


  Run Time X (second) |  Run time O (second) |  States Visited X | States Visited O | Winner
  :---: | :---: | :---: | :---: | :---: 
  0.008020860000000596 | 0.007300824999999733 | 819 | 578 | Draw
  0.007836479999999924 | 0.006701374999999565 | 1083 | 1156 | Draw
  0.004403000000000467 | 0.006689008333332931 | 1347 | 1734 | Draw
  
  
  ##### Min Max Cutt Off Agent 


  Run Time X (second) |  Run time O (second) |  States Visited X | States Visited O | Winner
  :---: | :---: | :---: | :---: | :---: 
  0.0253612999999995 | 0.015399450000000314  | 468 | 256 | Draw
  0.01614534000000125 | 0.015588750000000928 | 633 | 512 | Draw 
  0.013093246666667764 | 0.015564358333334619 | 798 | 768 | Draw  
  


#### 2.Number of expanded states, Execution time and Execution result for board 4x4

#### :arrow_down_small: Experiments and results:  
  
 ##### Min Max Alpha Beta Prunning Agent 


  Run Time X (second) |  Run time O (second) |  States Visited X | States Visited O | Winner
  :---: | :---: | :---: | :---: | :---: 
   0.02465118750000006 | 0.020783462500000183 | 2932  | 2294 | Draw 
   0.01990927500000078 | 0.019110718750000977 | 5010 | 4588 | Draw 
   0.018342691666668205 | 0.018484245833333596 | 7088 | 6882 | Draw
  
  ##### Min Max Cutt Off Agent 


  Run Time X (second) |  Run time O (second) |  States Visited X | States Visited O | Winner
  :---: | :---: | :---: | :---: | :---: 
  0.13512828749999994 | 0.09726290000000026 | 2567 | 2248 | Draw
  0.10862208124999972 | 0.09674043750000016 | 4534 | 4496 | Draw 
  0.10008275833333354 | 0.0970265624999999 | 6501 | 6744 | Draw 


#### 3. Number of expanded states, Execution time and Execution result for board 5x5

#### :arrow_down_small: Experiments and results:

    
 ##### Min Max Alpha Beta Prunning Agent 

   
  Run Time X (second) |  Run time O (second) |  States Visited X | States Visited O | Winner
  :---: | :---: | :---: | :---: | :---: 
   0.021876115384615424 | 0.021099149999999955  | 3281 | 3071 | Draw 
   0.019763750000001547 | 0.021189479166665654 | 6093 | 614 | Draw  
   0.01910204615384525 | 0.021263758333332036 | 8905 | 9213 | Draw
  
  ##### Min Max Cutt Off Agent 


  Run Time X (second) |  Run time O (second) |  States Visited X | States Visited O | Winner
  :---: | :---: | :---: | :---: | :---: 
  0.329658823076923 | 0.3123124 | 3608  | 3224 | Draw
  0.29569597307692325 | 0.31322052500000036 | 6526 | 6448 | Draw 
  0.282937802564102 | 0.31784044444444576 | 9444 | 9672 |  Draw


#### 4. 3 x 3 Algorithms Competition

#### :arrow_down_small: Experiments and results:

  Algorithm I | Algorithm II | Run Time X Algorithm I (second) |  Algorithm II Run time O (second) |  States Visited X | States Visited O | Winner
  :---: | :---: | :---: | :---: | :---: | :---: | :---:
  Min max | Min Max Alpha Beta | 7.65047436 | 0.009880799999999464 | 557487 | 846 | Draw
  Min max | Min Max Cutt Off |  7.614115340000002 | 0.016792000000000584 | 557487 | 276 | Draw
  Min Max Alpha Beta | Min Max | 0.00991497999999993 | 1.0421006249999998 | 819 | 60688 | Draw
  Min Max Alpha Beta | Min Max Cutt Off | 0.007781800000000061 | 0.017066499999999873 | 819 | 278 | Draw
  Min Max Cutt Off | Min Max |  0.025543020000000017 | 0.98045015 | 468 | 56490 | Draw
  Min Max Cutt Off | Min Max Alpha Beta | 0.03147322000000017 | 0.010567324999999794 | 468 | 921 | Draw
  
 
#### 5. 4 x 4 Algorithms Competition

#### :arrow_down_small: Experiments and results:

  Algorithm I | Algorithm II | Run Time X Algorithm I (second) |  Algorithm II Run time O (second) |  States Visited X | States Visited O | Winner
  :---: | :---: | :---: | :---: | :---: | :---: | :---:
  Min Max Alpha Beta | Min Max Cutt Off | 0.026708483333333238 | 0.13381676666666684 | 2415 | 2248 | O
  Min Max Cutt Off | Min Max Alpha Beta | 0.2380675000000001 | 0.03276520000000064 | 2061 | 1587 | X
  

#### 6. 5 x 5 Algorithms Competition

#### :arrow_down_small: Experiments and results:

  Algorithm I | Algorithm II | Run Time X Algorithm I (second) |  Algorithm II Run time O (second) |  States Visited X | States Visited O | Winner
  :---: | :---: | :---: | :---: | :---: | :---: | :---:
  Min Max Alpha Beta | Min Max Cutt Off | 0.023586953846153672 | 0.32774024166666665 | 3608 | 3145 | Draw
  Min Max Cutt Off | Min Max Alpha Beta | 0.32351358461538465  | 0.05862593333333329 | 3394 | 9002 | Draw
  

#### 7. Time Comparation Table
#### :arrow_down_small: Experiments and results:


![image](https://user-images.githubusercontent.com/74753713/136321836-f9a73971-14cb-4dcf-9097-315a5f0cd9d0.png)



#### 8. Time Comparation Graphic 
#### :arrow_down_small: Experiments and results:

![image](https://user-images.githubusercontent.com/74753713/136321861-1f5a9362-5509-4e02-9dbf-79e8b8f32b36.png)


#### 9. Nodes Expanded Comparation Table
#### :arrow_down_small: Experiments and results:


![image](https://user-images.githubusercontent.com/74753713/136322037-e78f6a43-4d52-4eda-8e5d-a8f07da64cde.png)




#### 10. Nodes Expanded Comparation Graphic 
#### :arrow_down_small: Experiments and results:

![image](https://user-images.githubusercontent.com/74753713/136322074-6d132932-1b28-4e42-a7fe-9295003a3327.png)





## CONCLUSION


## BIBLIOGRAPHY
* Class slides


