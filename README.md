# Projeto Final - Modelos Preditivos Conexionistas

### CAMILA CORRÊA DE MELO

|**DETECCAO**|**YOLOv5**|**PyTorch**|


## Performance

O modelo treinado possui performance de **84.7%**.

### Output do bloco de treinamento

<details>
  <summary>Click to expand!</summary>
  
  ```text
   Starting training for 1000 epochs...

           Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      0/399      14.2G     0.1139     0.0299    0.04146        104        640: 100% 7/7 [00:09<00:00,  1.38s/it]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:02<00:00,  2.48s/it]
                   all         40         50    0.00147      0.355    0.00273   0.000617

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      1/399      14.2G      0.101    0.02728     0.0411        119        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.07it/s]
                   all         40         50    0.00282      0.671     0.0103    0.00241

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      2/399      14.2G    0.08686    0.02569     0.0382        142        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.01it/s]
                   all         40         50    0.00352      0.827     0.0337     0.0101

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      3/399      14.2G    0.07464    0.02461    0.03568        119        640: 100% 7/7 [00:05<00:00,  1.32it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.18it/s]
                   all         40         50     0.0489      0.502      0.115     0.0442

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      4/399      14.2G    0.06744    0.02514    0.03236        105        640: 100% 7/7 [00:05<00:00,  1.31it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.52it/s]
                   all         40         50      0.669      0.342      0.357      0.128

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      5/399      14.2G    0.06201    0.02385     0.0306        118        640: 100% 7/7 [00:05<00:00,  1.29it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.61it/s]
                   all         40         50      0.701      0.427      0.419      0.143

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      6/399      14.2G    0.05681    0.02398    0.02724        106        640: 100% 7/7 [00:05<00:00,  1.30it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.63it/s]
                   all         40         50      0.644       0.42      0.526      0.229

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      7/399      14.2G    0.05503     0.0217    0.02408         97        640: 100% 7/7 [00:05<00:00,  1.31it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.51it/s]
                   all         40         50       0.45      0.689       0.67      0.342

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      8/399      14.2G    0.05438     0.0215    0.02174        114        640: 100% 7/7 [00:05<00:00,  1.32it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.58it/s]
                   all         40         50      0.653      0.614      0.704      0.286

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      9/399      14.2G    0.05165    0.01904    0.02007         83        640: 100% 7/7 [00:05<00:00,  1.27it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.63it/s]
                   all         40         50      0.702      0.566      0.625      0.278

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     10/399      14.2G    0.05468    0.01818    0.01823        110        640: 100% 7/7 [00:05<00:00,  1.28it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.80it/s]
                   all         40         50      0.517      0.599       0.61      0.241

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     11/399      14.2G    0.05266    0.01856    0.01839        144        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.66it/s]
                   all         40         50      0.657      0.563      0.655       0.33

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     12/399      14.2G    0.04875     0.0168    0.01568         81        640: 100% 7/7 [00:05<00:00,  1.30it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.44it/s]
                   all         40         50      0.616      0.739      0.659      0.211

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     13/399      14.2G    0.05193    0.01719    0.01616         87        640: 100% 7/7 [00:05<00:00,  1.28it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.73it/s]
                   all         40         50      0.521      0.567      0.572      0.206

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     14/399      14.2G    0.04876    0.01657    0.01809         87        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.50it/s]
                   all         40         50       0.63      0.693      0.659      0.361

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     15/399      14.2G    0.04946     0.0166    0.01408         88        640: 100% 7/7 [00:05<00:00,  1.22it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.98it/s]
                   all         40         50      0.465      0.573       0.49      0.236

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     16/399      14.2G    0.04619    0.01616    0.01469        107        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.94it/s]
                   all         40         50       0.32      0.558      0.441      0.173

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     17/399      14.2G    0.04426    0.01601    0.01745         97        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.78it/s]
                   all         40         50      0.405      0.646      0.546       0.25

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     18/399      14.2G    0.04462     0.0156    0.01476        121        640: 100% 7/7 [00:05<00:00,  1.22it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.52it/s]
                   all         40         50      0.478      0.582      0.494        0.2

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     19/399      14.2G    0.04387    0.01446    0.01564        112        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.03it/s]
                   all         40         50      0.435      0.541       0.52      0.192

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     20/399      14.2G    0.04421    0.01491    0.01624        110        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.69it/s]
                   all         40         50      0.474      0.634       0.59      0.267

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     21/399      14.2G    0.04272    0.01494    0.01511        105        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.87it/s]
                   all         40         50      0.514      0.552      0.498      0.232

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     22/399      14.2G    0.04114    0.01588    0.01309         94        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.69it/s]
                   all         40         50      0.564      0.665      0.596      0.342

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     23/399      14.2G    0.03868    0.01462    0.01307         88        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.74it/s]
                   all         40         50      0.573      0.835      0.651      0.367

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     24/399      14.2G     0.0418    0.01418    0.01438         98        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.65it/s]
                   all         40         50      0.684      0.632      0.645      0.374

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     25/399      14.2G    0.03997    0.01473     0.0141        117        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.53it/s]
                   all         40         50      0.708      0.676      0.687      0.353

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     26/399      14.2G    0.03883    0.01408    0.01197         82        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.59it/s]
                   all         40         50      0.739      0.774      0.755      0.408

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     27/399      14.2G    0.04165    0.01457    0.01497        105        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.94it/s]
                   all         40         50       0.81      0.703      0.769      0.351

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     28/399      14.2G    0.03691    0.01393    0.01512         97        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.81it/s]
                   all         40         50      0.502       0.44      0.345      0.181

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     29/399      14.2G    0.03929    0.01485    0.01294        132        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.71it/s]
                   all         40         50      0.776      0.805       0.74      0.452

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     30/399      14.2G    0.04013     0.0148     0.0144         98        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.47it/s]
                   all         40         50      0.718      0.788      0.733      0.448

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     31/399      14.2G    0.03804    0.01511    0.01019        107        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.52it/s]
                   all         40         50      0.757      0.736      0.695      0.481

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     32/399      14.2G    0.03693    0.01394    0.01359         96        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.85it/s]
                   all         40         50      0.783       0.85      0.808      0.523

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     33/399      14.2G     0.0343    0.01322    0.01362         81        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.78it/s]
                   all         40         50      0.722       0.71      0.767      0.459

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     34/399      14.2G    0.03561    0.01329    0.01231        108        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.46it/s]
                   all         40         50      0.692      0.682      0.645      0.408

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     35/399      14.2G    0.03523    0.01449    0.01136        121        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.81it/s]
                   all         40         50      0.726      0.781      0.764      0.472

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     36/399      14.2G    0.03566    0.01389    0.01391        110        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.10it/s]
                   all         40         50        0.8      0.804      0.736      0.493

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     37/399      14.2G    0.03517    0.01444    0.01155         93        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.49it/s]
                   all         40         50      0.739      0.892      0.814      0.414

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     38/399      14.2G    0.03528    0.01453    0.01327        110        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.68it/s]
                   all         40         50      0.688      0.876      0.796       0.46

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     39/399      14.2G    0.03431    0.01388    0.01179        111        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:02<00:00,  2.93s/it]
                   all         40         50      0.803      0.806      0.796      0.462

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     40/399      14.2G    0.03433    0.01316    0.01266         94        640: 100% 7/7 [00:05<00:00,  1.21it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.65it/s]
                   all         40         50      0.827      0.786      0.854      0.533

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     41/399      14.2G    0.03371    0.01304    0.01189         92        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.69it/s]
                   all         40         50      0.815      0.877      0.891      0.589

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     42/399      14.2G    0.03528    0.01417   0.009682        111        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.68it/s]
                   all         40         50      0.842      0.876      0.815      0.518

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     43/399      14.2G    0.03401    0.01341    0.01132        132        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.99it/s]
                   all         40         50      0.709      0.846      0.764      0.522

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     44/399      14.2G    0.03356    0.01345    0.01325        141        640: 100% 7/7 [00:05<00:00,  1.21it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.51it/s]
                   all         40         50      0.767      0.811      0.824       0.52

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     45/399      14.2G    0.03399    0.01284    0.01057        121        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.76it/s]
                   all         40         50      0.805      0.826      0.799      0.505

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     46/399      14.2G    0.03284    0.01392    0.01304        115        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.48it/s]
                   all         40         50      0.836      0.887      0.801      0.496

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     47/399      14.2G    0.03153    0.01328    0.01011         94        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.82it/s]
                   all         40         50      0.761      0.872      0.832      0.467

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     48/399      14.2G    0.03318    0.01315     0.0106         96        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.92it/s]
                   all         40         50      0.654      0.704       0.67      0.385

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     49/399      14.2G    0.03348     0.0128    0.00967         91        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.80it/s]
                   all         40         50      0.668      0.824      0.749      0.505

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     50/399      14.2G    0.03077    0.01194    0.01165        103        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.65it/s]
                   all         40         50      0.737      0.846      0.759       0.44

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     51/399      14.2G    0.03142    0.01265   0.009915         99        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.68it/s]
                   all         40         50      0.773      0.893      0.869      0.538

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     52/399      14.2G    0.03116    0.01344   0.009804         93        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.52it/s]
                   all         40         50      0.824      0.831      0.856      0.472

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     53/399      14.2G    0.03084    0.01317    0.01144        103        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.73it/s]
                   all         40         50       0.83      0.855      0.881      0.601

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     54/399      14.2G    0.02995     0.0131    0.01159        105        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.76it/s]
                   all         40         50      0.761      0.886      0.828      0.538

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     55/399      14.2G    0.03121     0.0125    0.01205         90        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.09it/s]
                   all         40         50      0.777      0.843      0.822      0.457

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     56/399      14.2G    0.03098     0.0125    0.01079         96        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.76it/s]
                   all         40         50      0.802      0.867      0.771      0.472

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     57/399      14.2G    0.03044    0.01302    0.01006        113        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.00it/s]
                   all         40         50      0.745      0.933      0.796      0.528

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     58/399      14.2G    0.03015    0.01223    0.01244        129        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.13it/s]
                   all         40         50      0.777      0.942      0.806      0.539

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     59/399      14.2G    0.03086    0.01235    0.01057        101        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.77it/s]
                   all         40         50       0.83      0.847      0.797      0.501

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     60/399      14.2G    0.03142    0.01249   0.009465         92        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.60it/s]
                   all         40         50      0.802        0.9      0.791      0.516

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     61/399      14.2G       0.03    0.01204    0.01293         89        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.76it/s]
                   all         40         50      0.822      0.881      0.851      0.541

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     62/399      14.2G    0.03002    0.01219     0.0124         97        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.63it/s]
                   all         40         50      0.766      0.937      0.822      0.521

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     63/399      14.2G    0.02896    0.01293       0.01         85        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.58it/s]
                   all         40         50      0.816      0.939      0.862      0.591

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     64/399      14.2G    0.03071    0.01259    0.01136        123        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.77it/s]
                   all         40         50      0.842      0.896      0.862      0.608

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     65/399      14.2G    0.02917    0.01228    0.01188        117        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.04it/s]
                   all         40         50       0.81       0.85        0.8      0.563

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     66/399      14.2G    0.02825    0.01276     0.0101        107        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.76it/s]
                   all         40         50      0.808      0.943      0.855      0.583

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     67/399      14.2G    0.02874    0.01264    0.01022        104        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.57it/s]
                   all         40         50      0.813      0.885      0.881      0.598

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     68/399      14.2G    0.02941     0.0121     0.0108         81        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.73it/s]
                   all         40         50      0.764      0.759      0.746      0.476

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     69/399      14.2G    0.03016    0.01182   0.009842        100        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.58it/s]
                   all         40         50      0.674      0.803      0.717      0.464

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     70/399      14.2G    0.02935    0.01213     0.0105         84        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.49it/s]
                   all         40         50      0.776      0.862      0.796       0.56

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     71/399      14.2G    0.02844    0.01183    0.01168        114        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.85it/s]
                   all         40         50      0.788      0.799      0.777      0.557

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     72/399      14.2G    0.02772     0.0125   0.008677        101        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.65it/s]
                   all         40         50      0.785      0.883      0.794      0.534

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     73/399      14.2G    0.02806    0.01287   0.009027        101        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.77it/s]
                   all         40         50      0.767      0.863      0.851      0.605

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     74/399      14.2G    0.03045     0.0122   0.009904         89        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.36it/s]
                   all         40         50      0.868      0.839      0.906      0.655

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     75/399      14.2G    0.02963    0.01247    0.01296        131        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.56it/s]
                   all         40         50      0.817      0.861      0.882      0.623

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     76/399      14.2G    0.02963    0.01133     0.0115         96        640: 100% 7/7 [00:05<00:00,  1.22it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.63it/s]
                   all         40         50      0.879      0.716      0.862      0.597

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     77/399      14.2G     0.0292    0.01241   0.009332        101        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.43it/s]
                   all         40         50      0.779      0.719      0.794      0.472

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     78/399      14.2G    0.02856    0.01385   0.009519        108        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.79it/s]
                   all         40         50      0.903      0.801      0.851      0.529

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     79/399      14.2G    0.02729    0.01205       0.01         93        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:02<00:00,  2.97s/it]
                   all         40         50      0.778      0.878      0.804      0.568

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     80/399      14.2G    0.02728    0.01178    0.00983        118        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.81it/s]
                   all         40         50      0.849      0.823      0.786      0.526

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     81/399      14.2G    0.02715      0.013    0.01011        136        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.72it/s]
                   all         40         50      0.851      0.919      0.836      0.542

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     82/399      14.2G    0.02688    0.01204   0.008878        104        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.75it/s]
                   all         40         50      0.837      0.921      0.889      0.597

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     83/399      14.2G    0.02801    0.01183    0.01135         90        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.85it/s]
                   all         40         50      0.843      0.946      0.893      0.615

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     84/399      14.2G    0.02679    0.01185   0.009919        101        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.68it/s]
                   all         40         50      0.823        0.8      0.846      0.558

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     85/399      14.2G    0.02773    0.01291   0.008986        125        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.98it/s]
                   all         40         50      0.855        0.7      0.799       0.55

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     86/399      14.2G    0.02683    0.01208    0.01029        106        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.77it/s]
                   all         40         50      0.817      0.883      0.874      0.611

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     87/399      14.2G    0.02643    0.01184    0.01016         77        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.79it/s]
                   all         40         50      0.834      0.858      0.861      0.612

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     88/399      14.2G     0.0279    0.01152   0.009815         90        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.60it/s]
                   all         40         50      0.785      0.823      0.846       0.58

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     89/399      14.2G    0.02753    0.01261   0.009358        117        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.52it/s]
                   all         40         50      0.773      0.882      0.884      0.618

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     90/399      14.2G    0.02766    0.01188    0.01232         87        640: 100% 7/7 [00:05<00:00,  1.22it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.56it/s]
                   all         40         50      0.775      0.817      0.807      0.597

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     91/399      14.2G     0.0267    0.01157    0.01091        111        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.51it/s]
                   all         40         50      0.896      0.748      0.829       0.56

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     92/399      14.2G    0.02704    0.01172    0.01039         97        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.79it/s]
                   all         40         50      0.867      0.782      0.843      0.561

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     93/399      14.2G    0.02559    0.01251   0.008252        141        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.88it/s]
                   all         40         50       0.81      0.734      0.829      0.534

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     94/399      14.2G    0.02545    0.01205    0.01037        116        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.05it/s]
                   all         40         50      0.823      0.883      0.848      0.573

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     95/399      14.2G    0.02589    0.01192   0.008892        112        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.63it/s]
                   all         40         50      0.869      0.872      0.884      0.595

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     96/399      14.2G     0.0265    0.01179   0.008054        100        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.81it/s]
                   all         40         50      0.895      0.828      0.876      0.599

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     97/399      14.2G    0.02347    0.01099    0.01043         98        640: 100% 7/7 [00:05<00:00,  1.27it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.45it/s]
                   all         40         50      0.921      0.796       0.85      0.601

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     98/399      14.2G    0.02514    0.01145    0.00889         93        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.73it/s]
                   all         40         50      0.846       0.82      0.845      0.587

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     99/399      14.2G    0.02559    0.01272   0.008101        101        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.52it/s]
                   all         40         50      0.844      0.864      0.866      0.606

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    100/399      14.2G    0.02623    0.01201   0.007641         93        640: 100% 7/7 [00:05<00:00,  1.17it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.58it/s]
                   all         40         50      0.843      0.796      0.851      0.614

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    101/399      14.2G    0.02525    0.01159   0.008405        108        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.72it/s]
                   all         40         50      0.747      0.924      0.829      0.573

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    102/399      14.2G    0.02438    0.01189    0.01014        116        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.51it/s]
                   all         40         50      0.725      0.922      0.844      0.596

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    103/399      14.2G    0.02607    0.01135   0.009884        107        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.72it/s]
                   all         40         50      0.882      0.778      0.887      0.617

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    104/399      14.2G     0.0258    0.01259   0.007367        109        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.58it/s]
                   all         40         50      0.826      0.867      0.875      0.606

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    105/399      14.2G    0.02576    0.01205   0.008585        102        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.93it/s]
                   all         40         50      0.817      0.857      0.838      0.578

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    106/399      14.2G    0.02781    0.01051    0.01002         97        640: 100% 7/7 [00:05<00:00,  1.22it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.63it/s]
                   all         40         50      0.843      0.941      0.861      0.552

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    107/399      14.2G    0.02487    0.01163   0.009105        101        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.67it/s]
                   all         40         50      0.841      0.946       0.86      0.567

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    108/399      14.2G    0.02725    0.01156    0.01028         76        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.71it/s]
                   all         40         50      0.818       0.85      0.884      0.605

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    109/399      14.2G    0.02648     0.0115   0.008975        113        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.77it/s]
                   all         40         50      0.862      0.798      0.872      0.634

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    110/399      14.2G    0.02482    0.01155   0.009859        109        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.74it/s]
                   all         40         50      0.863      0.806      0.856      0.609

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    111/399      14.2G    0.02527    0.01085    0.01045        117        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.75it/s]
                   all         40         50      0.869      0.792      0.888      0.625

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    112/399      14.2G    0.02547    0.01182   0.008293        137        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.56it/s]
                   all         40         50      0.812      0.828      0.838      0.604

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    113/399      14.2G    0.02416    0.01144   0.009645         95        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.86it/s]
                   all         40         50      0.784      0.797      0.787      0.577

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    114/399      14.2G    0.02533    0.01056   0.008234        104        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.56it/s]
                   all         40         50      0.739      0.856      0.779      0.562

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    115/399      14.2G    0.02602    0.01079   0.009188         94        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.66it/s]
                   all         40         50      0.746      0.842      0.791      0.552

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    116/399      14.2G    0.02335    0.01114    0.01229         69        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.74it/s]
                   all         40         50      0.814      0.854      0.848      0.582

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    117/399      14.2G    0.02368    0.01133   0.008253        106        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.81it/s]
                   all         40         50      0.816      0.832      0.852      0.611

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    118/399      14.2G    0.02438    0.01171   0.008743         95        640: 100% 7/7 [00:05<00:00,  1.27it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.68it/s]
                   all         40         50      0.777      0.895       0.87      0.624

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    119/399      14.2G    0.02473    0.01127   0.009042        137        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:02<00:00,  2.74s/it]
                   all         40         50      0.776       0.92      0.868      0.618

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    120/399      14.2G    0.02532    0.01096   0.009022         98        640: 100% 7/7 [00:05<00:00,  1.22it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.39it/s]
                   all         40         50      0.744      0.791      0.848      0.596

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    121/399      14.2G    0.02286    0.01174   0.008774        127        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.52it/s]
                   all         40         50      0.812      0.733      0.819       0.58

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    122/399      14.2G    0.02372    0.01176    0.01096        127        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.95it/s]
                   all         40         50      0.764      0.837      0.809      0.543

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    123/399      14.2G    0.02363    0.01104   0.009277        123        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.81it/s]
                   all         40         50      0.761      0.904      0.836      0.597

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    124/399      14.2G    0.02271    0.01141   0.008654         84        640: 100% 7/7 [00:05<00:00,  1.22it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.56it/s]
                   all         40         50      0.841      0.882      0.833      0.588

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    125/399      14.2G     0.0248    0.01133   0.008911        104        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.94it/s]
                   all         40         50      0.817      0.873       0.84      0.621

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    126/399      14.2G    0.02628     0.0128   0.007003        134        640: 100% 7/7 [00:05<00:00,  1.22it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.55it/s]
                   all         40         50      0.847      0.896      0.917      0.659

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    127/399      14.2G    0.02449    0.01142   0.008334         90        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.43it/s]
                   all         40         50      0.869      0.923      0.878      0.617

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    128/399      14.2G    0.02372     0.0114   0.009349        120        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.79it/s]
                   all         40         50      0.855      0.921      0.856      0.606

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    129/399      14.2G    0.02422    0.01092   0.008552        116        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.95it/s]
                   all         40         50      0.874        0.9      0.906      0.618

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    130/399      14.2G    0.02219    0.01107   0.008083        120        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.65it/s]
                   all         40         50      0.848      0.897      0.879      0.619

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    131/399      14.2G    0.02307    0.01138   0.009646         97        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.84it/s]
                   all         40         50      0.822      0.853      0.871      0.601

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    132/399      14.2G    0.02419    0.01129   0.008387        120        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.78it/s]
                   all         40         50      0.818      0.864      0.894      0.611

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    133/399      14.2G    0.02266     0.0115   0.009308        104        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.27it/s]
                   all         40         50      0.844      0.875      0.843      0.604

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    134/399      14.2G    0.02436    0.01085   0.008876         95        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.82it/s]
                   all         40         50      0.803      0.852      0.773      0.544

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    135/399      14.2G    0.02363    0.01119    0.00992        114        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.73it/s]
                   all         40         50      0.797      0.846      0.763      0.535

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    136/399      14.2G    0.02345    0.01094   0.008402        108        640: 100% 7/7 [00:05<00:00,  1.22it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.96it/s]
                   all         40         50      0.772       0.83      0.788      0.562

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    137/399      14.2G    0.02226    0.01031   0.009683        115        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.97it/s]
                   all         40         50      0.755      0.874        0.8       0.57

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    138/399      14.2G    0.02214     0.0106   0.009054         98        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.49it/s]
                   all         40         50      0.816      0.883      0.806      0.581

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    139/399      14.2G     0.0239    0.01042   0.008414        103        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.80it/s]
                   all         40         50      0.841      0.807      0.815      0.574

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    140/399      14.2G    0.02326    0.01068   0.008633         82        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.53it/s]
                   all         40         50       0.83      0.751      0.803      0.575

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    141/399      14.2G    0.02143    0.01118   0.009545        105        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.78it/s]
                   all         40         50      0.777       0.76      0.779      0.587

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    142/399      14.2G     0.0238    0.01049   0.009279        110        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.77it/s]
                   all         40         50        0.8      0.773      0.795       0.58

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    143/399      14.2G    0.02237    0.01107   0.009227        105        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.57it/s]
                   all         40         50        0.8      0.778        0.8      0.561

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    144/399      14.2G    0.02304     0.0109    0.01014        129        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.80it/s]
                   all         40         50      0.778      0.828      0.816      0.554

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    145/399      14.2G    0.02094    0.01047   0.009343        105        640: 100% 7/7 [00:05<00:00,  1.22it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.02it/s]
                   all         40         50      0.775      0.851      0.831      0.588

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    146/399      14.2G    0.02119   0.009701    0.01039         96        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.76it/s]
                   all         40         50      0.785      0.887      0.907      0.643

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    147/399      14.2G    0.02341    0.01186   0.007008        124        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.95it/s]
                   all         40         50      0.877      0.824      0.911      0.636

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    148/399      14.2G    0.02428    0.01095     0.0103         94        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.52it/s]
                   all         40         50      0.891      0.817      0.912      0.657

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    149/399      14.2G    0.02247    0.01146   0.009936        121        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.87it/s]
                   all         40         50      0.819      0.819      0.872      0.604

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    150/399      14.2G    0.02125    0.01127   0.009942        120        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.58it/s]
                   all         40         50       0.77      0.782      0.846      0.614

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    151/399      14.2G     0.0239    0.01137    0.01086        149        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.96it/s]
                   all         40         50      0.812      0.829      0.845       0.62

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    152/399      14.2G    0.02172    0.01055   0.008657        101        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.50it/s]
                   all         40         50      0.858      0.877      0.881      0.623

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    153/399      14.2G    0.02184    0.01064   0.008105        101        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.65it/s]
                   all         40         50      0.879      0.871      0.898      0.623

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    154/399      14.2G     0.0213    0.01044   0.007421        107        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.74it/s]
                   all         40         50       0.85      0.894      0.884      0.631

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    155/399      14.2G    0.02171    0.01081   0.008562         99        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.76it/s]
                   all         40         50      0.817      0.847       0.85      0.616

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    156/399      14.2G    0.02239    0.01132   0.007361        129        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.58it/s]
                   all         40         50      0.721      0.829      0.799       0.57

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    157/399      14.2G    0.02143    0.01031   0.007398        124        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.66it/s]
                   all         40         50      0.776      0.812      0.815      0.576

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    158/399      14.2G    0.02156    0.01024   0.008451         95        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.60it/s]
                   all         40         50      0.781      0.886      0.846      0.619

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    159/399      14.2G    0.02045    0.01009   0.009564        103        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:02<00:00,  2.72s/it]
                   all         40         50      0.796      0.846      0.818      0.606

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    160/399      14.2G    0.02076    0.01044   0.008269         98        640: 100% 7/7 [00:05<00:00,  1.20it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.55it/s]
                   all         40         50      0.823       0.87      0.841      0.633

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    161/399      14.2G    0.02121    0.01004   0.008857         93        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.50it/s]
                   all         40         50      0.781      0.771      0.765      0.576

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    162/399      14.2G    0.02033    0.01069   0.009147        111        640: 100% 7/7 [00:05<00:00,  1.27it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.47it/s]
                   all         40         50      0.704      0.825      0.738      0.545

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    163/399      14.2G    0.02098    0.01102    0.00832        113        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.10it/s]
                   all         40         50       0.75      0.855      0.863      0.626

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    164/399      14.2G    0.02097     0.0113   0.009668        126        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.63it/s]
                   all         40         50      0.796      0.896      0.857      0.604

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    165/399      14.2G    0.02153    0.01105   0.008592        120        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.06it/s]
                   all         40         50      0.806      0.919      0.834      0.567

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    166/399      14.2G     0.0212    0.01038   0.009729         99        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.72it/s]
                   all         40         50      0.824      0.917      0.846      0.589

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    167/399      14.2G    0.02196   0.009749    0.00902        120        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.05it/s]
                   all         40         50      0.837       0.87      0.843      0.594

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    168/399      14.2G    0.02274    0.01185   0.007522        119        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.57it/s]
                   all         40         50      0.803      0.921      0.826      0.546

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    169/399      14.2G    0.02287    0.01081   0.009083        100        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.07it/s]
                   all         40         50      0.814      0.908      0.855      0.578

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    170/399      14.2G    0.02244    0.01064   0.008149         93        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.87it/s]
                   all         40         50      0.883      0.904      0.913      0.613

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    171/399      14.2G    0.02227   0.009853    0.01001        112        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.28it/s]
                   all         40         50      0.875      0.897      0.905      0.646

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    172/399      14.2G    0.02309    0.01043   0.009701        108        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.58it/s]
                   all         40         50      0.865      0.908      0.886      0.627

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    173/399      14.2G     0.0216    0.01029   0.009511        112        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.57it/s]
                   all         40         50      0.807      0.911      0.881       0.64

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    174/399      14.2G    0.02281    0.01117    0.00812         87        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.77it/s]
                   all         40         50      0.809      0.904       0.82      0.571

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    175/399      14.2G    0.02209     0.0108   0.008944         96        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.92it/s]
                   all         40         50      0.803      0.903      0.823      0.557

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    176/399      14.2G    0.02183    0.01035   0.009896        104        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.25it/s]
                   all         40         50      0.834      0.867       0.87      0.579

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    177/399      14.2G    0.02125     0.0105     0.0105        109        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.23it/s]
                   all         40         50      0.789      0.867      0.852       0.61

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    178/399      14.2G      0.022    0.01132   0.008428        133        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.59it/s]
                   all         40         50       0.81      0.867      0.818      0.585

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    179/399      14.2G    0.02161    0.01116   0.008133         92        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.21it/s]
                   all         40         50      0.793      0.881      0.859      0.626

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    180/399      14.2G    0.02198    0.01083   0.007976         89        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.45it/s]
                   all         40         50      0.826      0.835      0.829      0.607

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    181/399      14.2G    0.02017    0.01016   0.006727         94        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.79it/s]
                   all         40         50      0.776      0.897      0.852      0.633

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    182/399      14.2G    0.02052     0.0092   0.009229        107        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.66it/s]
                   all         40         50       0.83      0.809      0.841      0.618

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    183/399      14.2G    0.02171    0.01037    0.00896        104        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.81it/s]
                   all         40         50      0.813      0.843      0.815      0.581

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    184/399      14.2G    0.02155    0.01036   0.007336        112        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.82it/s]
                   all         40         50      0.751      0.768      0.782      0.592

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    185/399      14.2G    0.02108    0.01052   0.007651        106        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.87it/s]
                   all         40         50      0.766      0.794      0.791      0.594

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    186/399      14.2G    0.01942   0.009853   0.008389        101        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.59it/s]
                   all         40         50      0.803      0.846      0.811      0.595

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    187/399      14.2G    0.02116    0.01093   0.009142         96        640: 100% 7/7 [00:06<00:00,  1.16it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.80it/s]
                   all         40         50      0.813      0.853      0.802      0.565

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    188/399      14.2G    0.02138     0.0116   0.008039        114        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.56it/s]
                   all         40         50      0.819       0.85      0.802      0.547

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    189/399      14.2G    0.01984    0.01041   0.008153        107        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.68it/s]
                   all         40         50      0.804      0.813      0.813      0.553

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    190/399      14.2G    0.02196   0.009815   0.008606         98        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.59it/s]
                   all         40         50       0.82      0.917      0.851      0.588

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    191/399      14.2G    0.02229   0.009854    0.01005        105        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.09it/s]
                   all         40         50      0.842      0.872      0.877      0.592

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    192/399      14.2G    0.02178    0.01075   0.009263        100        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.67it/s]
                   all         40         50      0.854      0.866      0.881      0.618

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    193/399      14.2G    0.02036   0.009842   0.009814         79        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.46it/s]
                   all         40         50       0.87      0.733      0.874      0.602

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    194/399      14.2G     0.0215    0.01097    0.01027        106        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.86it/s]
                   all         40         50      0.833      0.831      0.871      0.594

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    195/399      14.2G    0.02147    0.01098   0.009768        110        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.87it/s]
                   all         40         50      0.806      0.847      0.824      0.557

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    196/399      14.2G    0.02229    0.01053   0.008937        110        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.49it/s]
                   all         40         50      0.783      0.841      0.821      0.584

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    197/399      14.2G       0.02    0.01052   0.007331        108        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.04it/s]
                   all         40         50        0.8       0.89      0.864      0.609

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    198/399      14.2G     0.0202    0.01026    0.00746        106        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.81it/s]
                   all         40         50      0.769      0.925      0.854      0.626

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    199/399      14.2G    0.01908   0.009731   0.008247         89        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:02<00:00,  2.62s/it]
                   all         40         50      0.821      0.799      0.846       0.62

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    200/399      14.2G    0.02053    0.01001    0.01037        100        640: 100% 7/7 [00:05<00:00,  1.21it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.52it/s]
                   all         40         50      0.812      0.822      0.806        0.6

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    201/399      14.2G    0.01981   0.009747   0.009075        110        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.02it/s]
                   all         40         50      0.818      0.824      0.781      0.569

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    202/399      14.2G    0.02051    0.01022   0.008444        110        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.83it/s]
                   all         40         50      0.792      0.829      0.782      0.553

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    203/399      14.2G    0.02084    0.01037   0.008692        100        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.88it/s]
                   all         40         50      0.801      0.876      0.808      0.578

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    204/399      14.2G    0.02078   0.009962   0.008442        127        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.79it/s]
                   all         40         50      0.806      0.876      0.842      0.622

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    205/399      14.2G    0.01951   0.009425   0.007945         84        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.66it/s]
                   all         40         50      0.857      0.808      0.881       0.64

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    206/399      14.2G    0.01984    0.01003   0.007748        100        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.61it/s]
                   all         40         50      0.909      0.812      0.883      0.645

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    207/399      14.2G    0.01965   0.009806   0.007341        114        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.90it/s]
                   all         40         50      0.827      0.837      0.822      0.591

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    208/399      14.2G    0.01895   0.009846   0.007026        106        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.78it/s]
                   all         40         50      0.782      0.887      0.817      0.585

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    209/399      14.2G    0.02087   0.009777    0.01001        101        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.99it/s]
                   all         40         50      0.807       0.85      0.858      0.607

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    210/399      14.2G    0.01909   0.009792   0.008825        101        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.65it/s]
                   all         40         50      0.829      0.783      0.862      0.623

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    211/399      14.2G    0.02088   0.009959   0.009215        106        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.82it/s]
                   all         40         50      0.782      0.797      0.793      0.571

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    212/399      14.2G     0.0198   0.009676   0.008875         95        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.54it/s]
                   all         40         50      0.747      0.874      0.779      0.561

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    213/399      14.2G    0.02078   0.009083   0.009039        111        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.57it/s]
                   all         40         50      0.824      0.853      0.833      0.618

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    214/399      14.2G    0.01969    0.01105   0.007302        114        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.86it/s]
                   all         40         50      0.818      0.863      0.822       0.61

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    215/399      14.2G    0.02049    0.00977   0.008032        113        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.77it/s]
                   all         40         50      0.817      0.843      0.854      0.619

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    216/399      14.2G    0.02021    0.01054   0.005918        103        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.74it/s]
                   all         40         50      0.796      0.925       0.86      0.612

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    217/399      14.2G    0.01882    0.01022   0.008072        115        640: 100% 7/7 [00:05<00:00,  1.22it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.70it/s]
                   all         40         50      0.788       0.82       0.83      0.588

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    218/399      14.2G    0.01986   0.009745   0.009377        116        640: 100% 7/7 [00:05<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.50it/s]
                   all         40         50      0.747      0.767      0.814      0.595

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    219/399      14.2G    0.01812   0.009705   0.007436        103        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.64it/s]
                   all         40         50      0.714      0.764      0.775      0.557

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    220/399      14.2G    0.02009    0.01028   0.007095        105        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.70it/s]
                   all         40         50      0.759      0.821      0.825      0.594

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    221/399      14.2G    0.01951   0.009897   0.009573        128        640: 100% 7/7 [00:05<00:00,  1.27it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.71it/s]
                   all         40         50      0.896      0.783      0.881      0.644

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    222/399      14.2G    0.01932    0.01008     0.0106         86        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.52it/s]
                   all         40         50      0.852      0.818      0.855      0.631

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    223/399      14.2G    0.01957   0.009591   0.008636        106        640: 100% 7/7 [00:05<00:00,  1.25it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.74it/s]
                   all         40         50      0.875      0.778      0.857      0.624

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    224/399      14.2G    0.01868    0.01021   0.007491        108        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.94it/s]
                   all         40         50      0.816      0.885      0.875      0.643

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    225/399      14.2G    0.01934    0.01013   0.007652        107        640: 100% 7/7 [00:05<00:00,  1.24it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.91it/s]
                   all         40         50      0.838      0.883      0.862      0.642

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    226/399      14.2G     0.0189    0.01014   0.007805        116        640: 100% 7/7 [00:05<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.79it/s]
                   all         40         50      0.768      0.861      0.816      0.605
Stopping training early as no improvement observed in last 100 epochs. Best results observed at epoch 126, best model saved as best.pt.
To update EarlyStopping(patience=100) pass a new patience value, i.e. `python train.py --patience 300` or use `--patience 0` to disable EarlyStopping.

227 epochs completed in 0.435 hours.
Optimizer stripped from runs/train/exp/weights/last.pt, 14.5MB
Optimizer stripped from runs/train/exp/weights/best.pt, 14.5MB

Validating runs/train/exp/weights/best.pt...
Fusing layers... 
Model summary: 157 layers, 7018216 parameters, 0 gradients, 15.8 GFLOPs
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  2.32it/s]
                   all         40         50      0.847      0.897      0.917      0.659
             AMACIANTE         40         16          1      0.774      0.883      0.579
                 AVEIA         40         14      0.894          1      0.986      0.768
               SHAMPOO         40         20      0.647      0.916      0.882       0.63
  ```
</details>

### Evidências do treinamento

![Gráficos de Perdas](https://user-images.githubusercontent.com/115883399/200151062-d84d74ed-a59b-4d54-aa8e-f9482efeedfe.png)
![Matriz de Confusão](https://user-images.githubusercontent.com/115883399/200151039-0f7682df-7867-4676-85fc-f9fcfc0f16a5.png)

## Roboflow

[/especializacao/supermarket](https://universe.roboflow.com/especializao/supermarket-oqn4b)]

## HuggingFace

Nessa seção você deve publicar o link para o HuggingFace

