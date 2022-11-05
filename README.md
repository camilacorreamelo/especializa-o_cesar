# Projeto Final - Modelos Preditivos Conexionistas

### CAMILA CORRÊA DE MELO

|**DETECCAO**|**YOLOv5**|**PyTorch**|


## Performance

O modelo treinado possui performance de **92.3%*.

### Output do bloco de treinamento

<details>
  <summary>Click to expand!</summary>
  
  ```text
   Starting training for 1000 epochs...

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      0/999      11.4G     0.1073     0.0415    0.04064         29        640: 100% 16/16 [00:12<00:00,  1.26it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:02<00:00,  2.13s/it]
                   all         70        166    0.00437      0.598    0.00619     0.0015

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      1/999      12.9G    0.08608    0.03777    0.03518          9        640: 100% 16/16 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.32s/it]
                   all         70        166     0.0945      0.263     0.0911     0.0273

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      2/999      12.9G    0.07001    0.04531    0.02813         23        640: 100% 16/16 [00:09<00:00,  1.63it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.62s/it]
                   all         70        166      0.158      0.256      0.113     0.0257

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      3/999      12.9G    0.06202    0.03984     0.0209         11        640: 100% 16/16 [00:12<00:00,  1.30it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:02<00:00,  2.96s/it]
                   all         70        166      0.192      0.446      0.274      0.101

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      4/999      12.9G    0.06249    0.04078    0.01631         27        640: 100% 16/16 [00:12<00:00,  1.29it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.41s/it]
                   all         70        166      0.332      0.365      0.268     0.0814

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      5/999      12.9G     0.0622    0.03625     0.0133         18        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.54s/it]
                   all         70        166      0.497      0.599      0.507      0.162

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      6/999      12.9G    0.06232    0.03503    0.01393         18        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.73s/it]
                   all         70        166      0.341      0.561      0.362      0.136

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      7/999      12.9G    0.05604    0.03719    0.01467         29        640: 100% 16/16 [00:11<00:00,  1.39it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.87s/it]
                   all         70        166      0.265      0.349      0.207     0.0991

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      8/999      12.9G    0.05218    0.03367    0.01664         20        640: 100% 16/16 [00:09<00:00,  1.64it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.04s/it]
                   all         70        166        0.6      0.719      0.594      0.266

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      9/999      12.9G    0.04951     0.0334    0.01229         12        640: 100% 16/16 [00:09<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.04s/it]
                   all         70        166      0.609       0.56      0.575      0.258

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     10/999      12.9G    0.04756    0.03281    0.01171         37        640: 100% 16/16 [00:09<00:00,  1.63it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.14s/it]
                   all         70        166      0.465      0.673      0.564      0.228

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     11/999      12.9G     0.0451     0.0325    0.01162         26        640: 100% 16/16 [00:10<00:00,  1.59it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.26s/it]
                   all         70        166      0.647      0.674      0.716      0.359

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     12/999      12.9G    0.04372    0.02905    0.01316         12        640: 100% 16/16 [00:12<00:00,  1.31it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.16s/it]
                   all         70        166      0.761      0.623      0.727      0.376

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     13/999      12.9G    0.04217    0.03209    0.01293         15        640: 100% 16/16 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.25s/it]
                   all         70        166       0.62      0.614      0.636      0.302

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     14/999      12.9G    0.04033    0.03172    0.01109         56        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.27s/it]
                   all         70        166      0.752      0.679      0.758      0.397

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     15/999      12.9G    0.04288    0.03039    0.01051         16        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.35s/it]
                   all         70        166      0.862      0.786      0.866      0.428

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     16/999      12.9G    0.03987    0.03197    0.00889         47        640: 100% 16/16 [00:09<00:00,  1.64it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.77s/it]
                   all         70        166      0.911      0.761      0.898      0.492

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     17/999      12.9G    0.04324    0.02917   0.009803         29        640: 100% 16/16 [00:10<00:00,  1.50it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.25s/it]
                   all         70        166       0.81      0.649      0.763      0.463

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     18/999      12.9G    0.03946    0.02806    0.01071         27        640: 100% 16/16 [00:09<00:00,  1.63it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.21s/it]
                   all         70        166       0.84      0.516       0.61      0.352

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     19/999      12.9G      0.039    0.02902   0.009805          9        640: 100% 16/16 [00:09<00:00,  1.69it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.11s/it]
                   all         70        166      0.882      0.692      0.805      0.436

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     20/999      12.9G    0.03864    0.03038    0.01191          5        640: 100% 16/16 [00:10<00:00,  1.59it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.09s/it]
                   all         70        166      0.882      0.765      0.901      0.525

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     21/999      12.9G    0.03777    0.02813    0.01011          7        640: 100% 16/16 [00:12<00:00,  1.32it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.22s/it]
                   all         70        166      0.799      0.717      0.787      0.468

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     22/999      12.9G    0.03684    0.02998   0.008025         14        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.10s/it]
                   all         70        166      0.773      0.736      0.821      0.459

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     23/999      12.9G    0.03682    0.02914   0.009341         34        640: 100% 16/16 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.07s/it]
                   all         70        166      0.824      0.783       0.84      0.418

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     24/999      12.9G    0.03632    0.02888     0.0106         14        640: 100% 16/16 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.18s/it]
                   all         70        166       0.88      0.688      0.799      0.422

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     25/999      12.9G    0.03834    0.02835   0.009508         15        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.21s/it]
                   all         70        166      0.821      0.567      0.681      0.382

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     26/999      12.9G    0.03722    0.03195   0.007654         31        640: 100% 16/16 [00:12<00:00,  1.30it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.08s/it]
                   all         70        166      0.878      0.814      0.908      0.549

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     27/999      12.9G    0.03731    0.02934   0.007028         11        640: 100% 16/16 [00:09<00:00,  1.64it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         70        166      0.855      0.884      0.894      0.476

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     28/999      12.9G    0.03668    0.02737   0.009412         20        640: 100% 16/16 [00:09<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.05s/it]
                   all         70        166       0.84      0.768      0.804      0.428

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     29/999      12.9G    0.03621    0.02691   0.007742         23        640: 100% 16/16 [00:09<00:00,  1.63it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.08s/it]
                   all         70        166      0.871      0.803      0.894      0.521

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     30/999      12.9G    0.03358    0.02814   0.007271         16        640: 100% 16/16 [00:15<00:00,  1.04it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.69s/it]
                   all         70        166      0.908      0.835       0.89      0.561

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     31/999      12.9G    0.03432    0.02807   0.007652         14        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.26s/it]
                   all         70        166      0.919      0.825      0.908      0.565

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     32/999      12.9G     0.0334    0.02635   0.008869         13        640: 100% 16/16 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.05s/it]
                   all         70        166      0.899      0.869      0.922      0.533

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     33/999      12.9G    0.03435    0.02711   0.009039          2        640: 100% 16/16 [00:10<00:00,  1.57it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.02s/it]
                   all         70        166      0.912      0.797      0.891      0.529

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     34/999      12.9G    0.03516    0.03027   0.006165         30        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.13s/it]
                   all         70        166      0.873      0.758      0.865      0.501

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     35/999      12.9G    0.03487    0.02612    0.01162          9        640: 100% 16/16 [00:12<00:00,  1.32it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.23s/it]
                   all         70        166      0.878      0.845      0.907      0.536

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     36/999      12.9G    0.03421    0.02731   0.008451          5        640: 100% 16/16 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         70        166      0.825      0.814      0.872      0.455

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     37/999      12.9G    0.03115    0.02631   0.008866          5        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.08s/it]
                   all         70        166      0.894       0.84      0.914      0.527

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     38/999      12.9G    0.03556    0.02853   0.007259         20        640: 100% 16/16 [00:09<00:00,  1.64it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.29s/it]
                   all         70        166      0.803      0.754      0.881      0.552

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     39/999      12.9G    0.03405    0.02722   0.007824          7        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.23s/it]
                   all         70        166      0.902      0.858       0.91      0.525

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     40/999      12.9G    0.03509    0.02849   0.008775          5        640: 100% 16/16 [00:12<00:00,  1.32it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.20s/it]
                   all         70        166      0.937       0.79      0.913       0.55

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     41/999      12.9G    0.03416    0.02435   0.007563         18        640: 100% 16/16 [00:09<00:00,  1.64it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.24s/it]
                   all         70        166      0.873      0.889      0.917      0.551

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     42/999      12.9G    0.03448    0.03029   0.005975         36        640: 100% 16/16 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.16s/it]
                   all         70        166      0.908       0.81      0.902       0.55

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     43/999      12.9G    0.03057    0.02777   0.007102         21        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.26s/it]
                   all         70        166      0.865      0.826      0.903      0.521

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     44/999      12.9G    0.03125    0.02748   0.006421         38        640: 100% 16/16 [00:10<00:00,  1.56it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.73s/it]
                   all         70        166      0.923      0.849      0.914      0.536

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     45/999      12.9G    0.03188    0.02421   0.009726          4        640: 100% 16/16 [00:10<00:00,  1.59it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.25s/it]
                   all         70        166      0.873       0.82      0.893      0.569

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     46/999      12.9G    0.03165    0.02576    0.01113          7        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.18s/it]
                   all         70        166      0.896      0.853      0.924      0.576

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     47/999      12.9G    0.03495    0.02742   0.006987         41        640: 100% 16/16 [00:10<00:00,  1.56it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.04s/it]
                   all         70        166      0.854      0.862      0.878      0.562

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     48/999      12.9G    0.03162    0.02758     0.0087          6        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.15s/it]
                   all         70        166      0.922      0.866      0.921      0.521

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     49/999      12.9G    0.03087    0.02787   0.005612         18        640: 100% 16/16 [00:11<00:00,  1.38it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         70        166      0.905      0.862      0.904       0.56

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     50/999      12.9G    0.03064    0.02729   0.006269          8        640: 100% 16/16 [00:09<00:00,  1.60it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.23s/it]
                   all         70        166      0.912      0.836       0.89      0.533

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     51/999      12.9G    0.03204    0.02796   0.005827          9        640: 100% 16/16 [00:10<00:00,  1.59it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.15s/it]
                   all         70        166      0.824      0.831      0.899      0.529

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     52/999      12.9G    0.03364    0.02482   0.008575          9        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.22s/it]
                   all         70        166       0.89      0.818      0.908      0.544

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     53/999      12.9G    0.03363    0.02608   0.008475          6        640: 100% 16/16 [00:10<00:00,  1.58it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.59s/it]
                   all         70        166      0.903      0.878      0.929      0.571

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     54/999      12.9G    0.03084    0.02566   0.007076         20        640: 100% 16/16 [00:10<00:00,  1.49it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.26s/it]
                   all         70        166      0.858      0.845      0.902      0.562

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     55/999      12.9G     0.0316    0.02833   0.007156         23        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.20s/it]
                   all         70        166      0.809      0.824      0.861      0.557

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     56/999      12.9G    0.03101    0.02477    0.00673         10        640: 100% 16/16 [00:13<00:00,  1.18it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.39s/it]
                   all         70        166      0.902      0.904      0.932      0.576

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     57/999      12.9G    0.02967    0.02537    0.00765          8        640: 100% 16/16 [00:10<00:00,  1.57it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.32s/it]
                   all         70        166      0.901      0.827        0.9      0.537

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     58/999      12.9G    0.02954    0.02798   0.005699         30        640: 100% 16/16 [00:12<00:00,  1.33it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.38s/it]
                   all         70        166      0.896      0.859      0.907      0.573

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     59/999      12.9G    0.03049    0.02764   0.005632         28        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         70        166      0.929      0.856      0.921      0.591

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     60/999      12.9G    0.03161    0.02525   0.007491         32        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.27s/it]
                   all         70        166      0.916      0.881      0.938      0.595

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     61/999      12.9G    0.02991    0.02662   0.005862         17        640: 100% 16/16 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.24s/it]
                   all         70        166      0.892      0.868       0.93      0.565

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     62/999      12.9G    0.03184    0.02506     0.0102          5        640: 100% 16/16 [00:10<00:00,  1.55it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.72s/it]
                   all         70        166      0.914      0.858      0.922       0.52

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     63/999      12.9G    0.02908    0.02398   0.007004         12        640: 100% 16/16 [00:10<00:00,  1.55it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.15s/it]
                   all         70        166      0.903       0.82        0.9      0.556

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     64/999      12.9G    0.03049    0.02514     0.0077          6        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.23s/it]
                   all         70        166       0.87      0.846      0.879       0.53

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     65/999      12.9G    0.02895    0.02503   0.005403          4        640: 100% 16/16 [00:09<00:00,  1.64it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.09s/it]
                   all         70        166      0.869      0.791      0.849      0.504

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     66/999      12.9G    0.02973    0.02931   0.006803         44        640: 100% 16/16 [00:10<00:00,  1.59it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.24s/it]
                   all         70        166      0.858      0.844        0.9      0.591

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     67/999      12.9G    0.02921    0.02911   0.006191         58        640: 100% 16/16 [00:12<00:00,  1.32it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.13s/it]
                   all         70        166      0.822      0.839      0.893      0.566

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     68/999      12.9G    0.02897    0.02355   0.007293          3        640: 100% 16/16 [00:10<00:00,  1.58it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.04s/it]
                   all         70        166      0.901      0.868      0.912      0.561

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     69/999      12.9G    0.03077    0.02539    0.01083          8        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.16s/it]
                   all         70        166      0.892      0.838      0.881      0.568

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     70/999      12.9G    0.03123    0.02503   0.008084          9        640: 100% 16/16 [00:10<00:00,  1.59it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.17s/it]
                   all         70        166      0.921       0.76      0.866      0.559

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     71/999      12.9G    0.03171    0.02951   0.006445         74        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         70        166      0.902      0.805      0.885      0.543

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     72/999      12.9G    0.02948    0.02537   0.006434         26        640: 100% 16/16 [00:11<00:00,  1.37it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.16s/it]
                   all         70        166      0.825      0.839      0.864      0.538

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     73/999      12.9G    0.02869    0.02772   0.005108         14        640: 100% 16/16 [00:10<00:00,  1.56it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.07s/it]
                   all         70        166       0.89       0.85      0.907      0.539

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     74/999      12.9G    0.02944    0.02497   0.006683         16        640: 100% 16/16 [00:09<00:00,  1.60it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.11s/it]
                   all         70        166      0.899      0.844      0.894      0.578

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     75/999      12.9G    0.03305    0.02559   0.005236         14        640: 100% 16/16 [00:10<00:00,  1.59it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.18s/it]
                   all         70        166      0.889      0.872      0.909      0.579

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     76/999      12.9G     0.0308    0.02583    0.00632         36        640: 100% 16/16 [00:12<00:00,  1.33it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.17s/it]
                   all         70        166        0.9       0.82      0.889      0.583

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     77/999      12.9G    0.02962    0.02513   0.007403          8        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.24s/it]
                   all         70        166        0.9      0.794      0.878      0.565

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     78/999      12.9G    0.02959    0.02562   0.007205          9        640: 100% 16/16 [00:10<00:00,  1.59it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.20s/it]
                   all         70        166      0.905      0.874       0.91      0.607

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     79/999      12.9G    0.02872    0.02828   0.005072         38        640: 100% 16/16 [00:10<00:00,  1.56it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.03s/it]
                   all         70        166        0.9      0.881      0.922      0.612

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     80/999      12.9G    0.02876    0.02603   0.006584          5        640: 100% 16/16 [00:10<00:00,  1.53it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.05it/s]
                   all         70        166      0.881       0.85      0.923      0.547

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     81/999      12.9G    0.02891    0.02533   0.007293          6        640: 100% 16/16 [00:11<00:00,  1.36it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.29s/it]
                   all         70        166      0.917       0.85      0.916      0.593

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     82/999      12.9G    0.02938    0.02654    0.00617         19        640: 100% 16/16 [00:13<00:00,  1.15it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.16s/it]
                   all         70        166        0.9      0.847      0.917      0.567

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     83/999      12.9G    0.02925    0.02869   0.007095         34        640: 100% 16/16 [00:10<00:00,  1.60it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.17s/it]
                   all         70        166      0.889      0.825      0.907      0.569

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     84/999      12.9G    0.02871    0.02571   0.005639         20        640: 100% 16/16 [00:10<00:00,  1.51it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.07s/it]
                   all         70        166      0.886      0.835      0.895      0.552

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     85/999      12.9G    0.02943    0.02472   0.006229         13        640: 100% 16/16 [00:11<00:00,  1.36it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.29s/it]
                   all         70        166      0.899       0.85      0.925      0.604

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     86/999      12.9G    0.02878    0.02737   0.005623         27        640: 100% 16/16 [00:10<00:00,  1.59it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.05s/it]
                   all         70        166       0.86       0.86        0.9      0.576

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     87/999      12.9G    0.02859    0.02744   0.007027         23        640: 100% 16/16 [00:10<00:00,  1.54it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.14s/it]
                   all         70        166      0.892      0.795      0.899       0.55

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     88/999      12.9G     0.0283    0.02599   0.006063         38        640: 100% 16/16 [00:10<00:00,  1.59it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.06it/s]
                   all         70        166      0.885       0.87       0.93      0.619

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     89/999      12.9G     0.0276    0.02606   0.006474         10        640: 100% 16/16 [00:10<00:00,  1.45it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.59s/it]
                   all         70        166      0.902      0.902      0.942       0.61

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     90/999      12.9G    0.02757     0.0253   0.006235         10        640: 100% 16/16 [00:10<00:00,  1.56it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.22s/it]
                   all         70        166      0.915      0.814      0.911      0.601

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     91/999      12.9G    0.02802    0.02769   0.005385         54        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         70        166      0.895      0.861      0.916      0.604

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     92/999      12.9G    0.02702    0.02398   0.004981         13        640: 100% 16/16 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.22s/it]
                   all         70        166      0.931      0.855      0.919      0.602

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     93/999      12.9G    0.02986    0.02553   0.007252         11        640: 100% 16/16 [00:09<00:00,  1.63it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.01s/it]
                   all         70        166      0.879      0.843      0.914      0.573

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     94/999      12.9G     0.0272    0.02372   0.006093         13        640: 100% 16/16 [00:11<00:00,  1.36it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         70        166      0.971      0.821      0.932      0.596

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     95/999      12.9G    0.02654    0.02549   0.004933         25        640: 100% 16/16 [00:09<00:00,  1.63it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         70        166      0.915      0.871       0.93      0.583

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     96/999      12.9G    0.02835    0.02618   0.005466         22        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.15s/it]
                   all         70        166      0.851      0.809      0.854      0.564

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     97/999      12.9G    0.02746    0.02483   0.007061         16        640: 100% 16/16 [00:10<00:00,  1.56it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.02it/s]
                   all         70        166      0.952      0.898      0.941      0.608

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     98/999      12.9G    0.02659    0.02526   0.005747         19        640: 100% 16/16 [00:09<00:00,  1.63it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.14s/it]
                   all         70        166      0.904       0.89      0.934      0.585

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     99/999      12.9G    0.02842    0.02405    0.00678         19        640: 100% 16/16 [00:11<00:00,  1.39it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:03<00:00,  3.61s/it]
                   all         70        166      0.915      0.879      0.936      0.615

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    100/999      12.9G     0.0283    0.02553   0.006001         12        640: 100% 16/16 [00:10<00:00,  1.51it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.17s/it]
                   all         70        166       0.89      0.849      0.919      0.617

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    101/999      12.9G    0.02748    0.02396   0.005455         22        640: 100% 16/16 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         70        166      0.897      0.861      0.908       0.59

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    102/999      12.9G    0.02742    0.02381   0.005212         16        640: 100% 16/16 [00:09<00:00,  1.63it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.09s/it]
                   all         70        166      0.937      0.847      0.919       0.59

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    103/999      12.9G    0.02628    0.02469   0.004977         33        640: 100% 16/16 [00:11<00:00,  1.43it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.46s/it]
                   all         70        166       0.86       0.85      0.897      0.556

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    104/999      12.9G    0.02612    0.02406   0.008882          4        640: 100% 16/16 [00:10<00:00,  1.54it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.04it/s]
                   all         70        166      0.842      0.821      0.876       0.55

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    105/999      12.9G    0.02787    0.02617   0.004737         52        640: 100% 16/16 [00:10<00:00,  1.55it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.91s/it]
                   all         70        166      0.888      0.844      0.901       0.53

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    106/999      12.9G    0.02736    0.02391   0.006872         15        640: 100% 16/16 [00:12<00:00,  1.32it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.47s/it]
                   all         70        166      0.931      0.882       0.93      0.609

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    107/999      12.9G     0.0273    0.02298   0.005519          8        640: 100% 16/16 [00:10<00:00,  1.51it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.93s/it]
                   all         70        166      0.861      0.874      0.922       0.56

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    108/999      12.9G    0.02783    0.02425   0.007001         20        640: 100% 16/16 [00:11<00:00,  1.38it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.12s/it]
                   all         70        166      0.887      0.837      0.882      0.568

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    109/999      12.9G    0.02759    0.02643   0.006044         27        640: 100% 16/16 [00:10<00:00,  1.46it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.25s/it]
                   all         70        166      0.926      0.814      0.855      0.564

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    110/999      12.9G    0.02639    0.02682   0.005712         67        640: 100% 16/16 [00:11<00:00,  1.45it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.30s/it]
                   all         70        166      0.903      0.849      0.921      0.599

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    111/999      12.9G    0.02586    0.02393   0.005923         12        640: 100% 16/16 [00:10<00:00,  1.47it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.26s/it]
                   all         70        166      0.884      0.852      0.903      0.587

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    112/999      12.9G    0.02629    0.02507   0.007434         14        640: 100% 16/16 [00:13<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.24s/it]
                   all         70        166      0.884      0.843      0.904      0.603

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    113/999      12.9G     0.0262      0.023   0.006371         17        640: 100% 16/16 [00:10<00:00,  1.48it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.08s/it]
                   all         70        166      0.939      0.849      0.905      0.572

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    114/999      12.9G    0.02704    0.02532   0.006206          8        640: 100% 16/16 [00:10<00:00,  1.50it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.33s/it]
                   all         70        166      0.882      0.852      0.915      0.606

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    115/999      12.9G    0.02681    0.02459    0.00562         10        640: 100% 16/16 [00:10<00:00,  1.46it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.22s/it]
                   all         70        166      0.925      0.836      0.907      0.579

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    116/999      12.9G    0.02729     0.0258   0.005572         48        640: 100% 16/16 [00:13<00:00,  1.19it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.28s/it]
                   all         70        166       0.86      0.816      0.882      0.591

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    117/999      12.9G    0.02724    0.02406   0.005641         10        640: 100% 16/16 [00:10<00:00,  1.53it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.24s/it]
                   all         70        166      0.909      0.886      0.904      0.572

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    118/999      12.9G    0.02661    0.02472   0.005322         20        640: 100% 16/16 [00:10<00:00,  1.50it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.40s/it]
                   all         70        166      0.888      0.873      0.919      0.594

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    119/999      12.9G    0.02714    0.02525   0.005963          6        640: 100% 16/16 [00:10<00:00,  1.49it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.37s/it]
                   all         70        166      0.919      0.885      0.922      0.601

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    120/999      12.9G    0.02665    0.02471   0.006243         27        640: 100% 16/16 [00:12<00:00,  1.31it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.47s/it]
                   all         70        166      0.839      0.878      0.909      0.601

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    121/999      12.9G    0.02736    0.02259   0.006025         12        640: 100% 16/16 [00:10<00:00,  1.52it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.33s/it]
                   all         70        166      0.888      0.838      0.891      0.582

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    122/999      12.9G    0.02683    0.02412   0.005391         10        640: 100% 16/16 [00:10<00:00,  1.50it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.25s/it]
                   all         70        166      0.878      0.818      0.895      0.571

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    123/999      12.9G    0.02857    0.02268   0.008216          2        640: 100% 16/16 [00:10<00:00,  1.59it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.11s/it]
                   all         70        166       0.91      0.853      0.913      0.598

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    124/999      12.9G    0.02637    0.02248   0.006073         14        640: 100% 16/16 [00:10<00:00,  1.56it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.33s/it]
                   all         70        166      0.943      0.874      0.925      0.591

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    125/999      12.9G    0.02658    0.02391   0.005092         19        640: 100% 16/16 [00:12<00:00,  1.33it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.27s/it]
                   all         70        166      0.938      0.904       0.94      0.601

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    126/999      12.9G     0.0264    0.02223   0.005016         11        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.13s/it]
                   all         70        166      0.928      0.894      0.943      0.602

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    127/999      12.9G    0.02576    0.02349   0.005137          4        640: 100% 16/16 [00:10<00:00,  1.54it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.04s/it]
                   all         70        166      0.938      0.901      0.946      0.612

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    128/999      12.9G    0.02756    0.02349   0.008086          7        640: 100% 16/16 [00:13<00:00,  1.17it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.04s/it]
                   all         70        166      0.917      0.839      0.917      0.592

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    129/999      12.9G    0.02629    0.02526   0.004747         25        640: 100% 16/16 [00:12<00:00,  1.28it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.31s/it]
                   all         70        166       0.91      0.835      0.909        0.6

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    130/999      12.9G    0.02596    0.02736   0.006022         35        640: 100% 16/16 [00:10<00:00,  1.57it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.17s/it]
                   all         70        166      0.882      0.898      0.918      0.602

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    131/999      12.9G    0.02553    0.02272   0.005395         15        640: 100% 16/16 [00:10<00:00,  1.59it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.24s/it]
                   all         70        166      0.907       0.81      0.909      0.614

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    132/999      12.9G    0.02639    0.02334   0.005128         17        640: 100% 16/16 [00:10<00:00,  1.57it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.28s/it]
                   all         70        166      0.889      0.865      0.926        0.6

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    133/999      12.9G    0.02631    0.02535   0.005641         58        640: 100% 16/16 [00:11<00:00,  1.37it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.33s/it]
                   all         70        166      0.952      0.813      0.912       0.57

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    134/999      12.9G    0.02602    0.02333   0.006133         11        640: 100% 16/16 [00:10<00:00,  1.53it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         70        166      0.906      0.835      0.888      0.581

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    135/999      12.9G    0.02609    0.02463   0.006781         22        640: 100% 16/16 [00:10<00:00,  1.56it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.17s/it]
                   all         70        166      0.887      0.805      0.869       0.54

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    136/999      12.9G    0.02463    0.02105   0.007041         12        640: 100% 16/16 [00:10<00:00,  1.56it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.14s/it]
                   all         70        166      0.892      0.851      0.889      0.577

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    137/999      12.9G    0.02705    0.02311   0.005617         24        640: 100% 16/16 [00:10<00:00,  1.54it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         70        166      0.868      0.888      0.902      0.602

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    138/999      12.9G     0.0269    0.02287   0.005261         19        640: 100% 16/16 [00:11<00:00,  1.36it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         70        166       0.92      0.831      0.892      0.587

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    139/999      12.9G    0.02743    0.02435   0.005701         20        640: 100% 16/16 [00:10<00:00,  1.54it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.08s/it]
                   all         70        166      0.894      0.852       0.88      0.569

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    140/999      12.9G    0.02633    0.02389   0.005938         33        640: 100% 16/16 [00:09<00:00,  1.60it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         70        166      0.922      0.879      0.917      0.577

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    141/999      12.9G    0.02497    0.02499   0.007724          4        640: 100% 16/16 [00:10<00:00,  1.57it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.13s/it]
                   all         70        166      0.941      0.892      0.912      0.596

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    142/999      12.9G    0.02468    0.02185    0.00601         12        640: 100% 16/16 [00:11<00:00,  1.43it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.71s/it]
                   all         70        166      0.927      0.853      0.896      0.609

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    143/999      12.9G    0.02563    0.02316   0.006031         22        640: 100% 16/16 [00:10<00:00,  1.53it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.11s/it]
                   all         70        166      0.918      0.841      0.893      0.596

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    144/999      12.9G    0.02524    0.02192   0.005033         15        640: 100% 16/16 [00:10<00:00,  1.54it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.10s/it]
                   all         70        166       0.91      0.829      0.898      0.597

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    145/999      12.9G    0.02509    0.02435   0.006067          5        640: 100% 16/16 [00:10<00:00,  1.54it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         70        166      0.925      0.861      0.918      0.604

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    146/999      12.9G    0.02566    0.02245   0.005946          8        640: 100% 16/16 [00:10<00:00,  1.54it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.14s/it]
                   all         70        166      0.901      0.869      0.912        0.6

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    147/999      12.9G    0.02632    0.02135   0.008064         12        640: 100% 16/16 [00:12<00:00,  1.31it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.11s/it]
                   all         70        166      0.883       0.86      0.905      0.601

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    148/999      12.9G    0.02587    0.02451    0.00562         10        640: 100% 16/16 [00:10<00:00,  1.57it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.24s/it]
                   all         70        166      0.878      0.864      0.909      0.602

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    149/999      12.9G    0.02523    0.02334   0.004836          8        640: 100% 16/16 [00:10<00:00,  1.54it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         70        166      0.906      0.865      0.921      0.576

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    150/999      12.9G    0.02753    0.02533   0.005408         36        640: 100% 16/16 [00:10<00:00,  1.58it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.27s/it]
                   all         70        166      0.899      0.813      0.864      0.565

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    151/999      12.9G    0.02608    0.02334   0.004784         22        640: 100% 16/16 [00:12<00:00,  1.32it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.18s/it]
                   all         70        166      0.896      0.844      0.896      0.585

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    152/999      12.9G    0.02595    0.02418   0.006339         33        640: 100% 16/16 [00:10<00:00,  1.60it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.04it/s]
                   all         70        166       0.91      0.838      0.871      0.568

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    153/999      12.9G     0.0264    0.02357   0.007137          7        640: 100% 16/16 [00:11<00:00,  1.41it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.81s/it]
                   all         70        166      0.866      0.838      0.894      0.567

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    154/999      12.9G    0.02622     0.0251   0.005676         43        640: 100% 16/16 [00:11<00:00,  1.37it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.14s/it]
                   all         70        166      0.903      0.865      0.903      0.552

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    155/999      12.9G    0.02445    0.02327   0.005993          8        640: 100% 16/16 [00:12<00:00,  1.28it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.46s/it]
                   all         70        166      0.882      0.829      0.902      0.582

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    156/999      12.9G    0.02538    0.02505   0.004739         35        640: 100% 16/16 [00:10<00:00,  1.58it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.09s/it]
                   all         70        166       0.92      0.855      0.893      0.576

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    157/999      12.9G    0.02559    0.02385   0.005791         17        640: 100% 16/16 [00:10<00:00,  1.51it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.26s/it]
                   all         70        166      0.863      0.835      0.899      0.578

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    158/999      12.9G    0.02677    0.02318   0.006987         44        640: 100% 16/16 [00:10<00:00,  1.51it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.11s/it]
                   all         70        166      0.901      0.873       0.92      0.614

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    159/999      12.9G    0.02619    0.02101   0.007856         14        640: 100% 16/16 [00:10<00:00,  1.57it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.25s/it]
                   all         70        166      0.918      0.806      0.906      0.594

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    160/999      12.9G    0.02645    0.02478   0.004972          6        640: 100% 16/16 [00:12<00:00,  1.33it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.11s/it]
                   all         70        166      0.832      0.872      0.898      0.593

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    161/999      12.9G    0.02494    0.02226    0.00749         10        640: 100% 16/16 [00:10<00:00,  1.54it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.30s/it]
                   all         70        166      0.906      0.875      0.924      0.611

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    162/999      12.9G    0.02515    0.02213   0.006459         10        640: 100% 16/16 [00:09<00:00,  1.60it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.14s/it]
                   all         70        166      0.883      0.795      0.838      0.566

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    163/999      12.9G     0.0242    0.02476   0.004198         32        640: 100% 16/16 [00:10<00:00,  1.54it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.27s/it]
                   all         70        166      0.904      0.833      0.907      0.588

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    164/999      12.9G    0.02667    0.02479   0.004974          9        640: 100% 16/16 [00:12<00:00,  1.32it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.18s/it]
                   all         70        166      0.879       0.81      0.896      0.592

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    165/999      12.9G     0.0257    0.02343   0.005229         29        640: 100% 16/16 [00:10<00:00,  1.59it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.05it/s]
                   all         70        166      0.945       0.79      0.904      0.602

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    166/999      12.9G    0.02573    0.02391   0.004429         26        640: 100% 16/16 [00:10<00:00,  1.53it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.36s/it]
                   all         70        166      0.937      0.848      0.921      0.613

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    167/999      12.9G    0.02442    0.02124   0.005391          4        640: 100% 16/16 [00:09<00:00,  1.63it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.16s/it]
                   all         70        166      0.919      0.837       0.92      0.612

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    168/999      12.9G    0.02682    0.02079   0.006071          9        640: 100% 16/16 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.21s/it]
                   all         70        166      0.864      0.846      0.899      0.569

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    169/999      12.9G    0.02505    0.02254   0.005346         18        640: 100% 16/16 [00:11<00:00,  1.42it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.18s/it]
                   all         70        166      0.901      0.912      0.939      0.612

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    170/999      12.9G    0.02495    0.02112   0.004719         11        640: 100% 16/16 [00:10<00:00,  1.57it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.03s/it]
                   all         70        166        0.9      0.888      0.922      0.596

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    171/999      12.9G    0.02555    0.02289   0.006041         12        640: 100% 16/16 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.23s/it]
                   all         70        166      0.868      0.855      0.915      0.601

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    172/999      12.9G     0.0247    0.02331   0.006671         18        640: 100% 16/16 [00:10<00:00,  1.53it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.08s/it]
                   all         70        166       0.83      0.861       0.86      0.565

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    173/999      12.9G    0.02409    0.02314      0.005         20        640: 100% 16/16 [00:11<00:00,  1.35it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.24s/it]
                   all         70        166      0.905      0.816      0.878       0.57

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    174/999      12.9G     0.0249    0.02398   0.004585         39        640: 100% 16/16 [00:10<00:00,  1.58it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.09it/s]
                   all         70        166      0.919      0.847      0.895      0.585

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    175/999      12.9G    0.02513    0.02344   0.006128         16        640: 100% 16/16 [00:10<00:00,  1.58it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.21s/it]
                   all         70        166      0.901      0.848      0.901      0.608

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    176/999      12.9G    0.02361    0.02188   0.004687         24        640: 100% 16/16 [00:10<00:00,  1.60it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.68s/it]
                   all         70        166      0.897      0.868      0.905       0.61

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    177/999      12.9G    0.02433    0.02161    0.00558         28        640: 100% 16/16 [00:13<00:00,  1.18it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.07s/it]
                   all         70        166      0.905      0.842      0.907      0.586

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    178/999      12.9G    0.02526     0.0239   0.007378          9        640: 100% 16/16 [00:10<00:00,  1.58it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.02it/s]
                   all         70        166      0.939      0.875      0.931      0.629

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    179/999      12.9G     0.0255    0.02521    0.00476         12        640: 100% 16/16 [00:09<00:00,  1.63it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.18s/it]
                   all         70        166      0.909      0.866      0.902        0.6

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    180/999      12.9G    0.02571    0.02208   0.006641          6        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.08s/it]
                   all         70        166      0.933      0.858      0.913      0.612

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    181/999      12.9G    0.02323    0.02127    0.00514          9        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.10s/it]
                   all         70        166      0.914      0.897      0.924      0.617

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    182/999      12.9G    0.02553    0.02592   0.004932         41        640: 100% 16/16 [00:11<00:00,  1.39it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.10s/it]
                   all         70        166      0.847      0.806      0.853      0.576

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    183/999      12.9G    0.02633    0.02298   0.005419         12        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.04s/it]
                   all         70        166      0.928       0.81      0.884        0.6

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    184/999      12.9G    0.02479    0.02193   0.005781         23        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.14s/it]
                   all         70        166      0.895       0.77      0.848      0.562

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    185/999      12.9G    0.02531    0.02319     0.0055         13        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.04s/it]
                   all         70        166      0.964      0.803      0.887      0.595

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    186/999      12.9G    0.02467    0.02376   0.006991         26        640: 100% 16/16 [00:09<00:00,  1.64it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.17s/it]
                   all         70        166      0.882      0.793      0.891      0.587

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    187/999      12.9G      0.025    0.02288   0.004925          7        640: 100% 16/16 [00:11<00:00,  1.42it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.03s/it]
                   all         70        166      0.879      0.844      0.871      0.577

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    188/999      12.9G     0.0256    0.02094   0.005437         18        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         70        166       0.88      0.848      0.863      0.561

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    189/999      12.9G    0.02597    0.02219   0.005339         11        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.00it/s]
                   all         70        166      0.878      0.806      0.853      0.539

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    190/999      12.9G    0.02473    0.02363    0.00492         19        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.08s/it]
                   all         70        166      0.896      0.853      0.894      0.559

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    191/999      12.9G    0.02438    0.02127   0.005407          8        640: 100% 16/16 [00:09<00:00,  1.64it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.64s/it]
                   all         70        166      0.945      0.838      0.915      0.597

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    192/999      12.9G    0.02489    0.02135   0.005667         25        640: 100% 16/16 [00:10<00:00,  1.56it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.24s/it]
                   all         70        166      0.935      0.847      0.911      0.605

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    193/999      12.9G    0.02456    0.02384   0.004536         21        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.09s/it]
                   all         70        166      0.885      0.845      0.877      0.589

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    194/999      12.9G    0.02463    0.02194   0.004952         18        640: 100% 16/16 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.01it/s]
                   all         70        166      0.924       0.85      0.913      0.608

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    195/999      12.9G    0.02401     0.0224   0.005906         14        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.08s/it]
                   all         70        166       0.89      0.833      0.876       0.58

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    196/999      12.9G    0.02537    0.02327   0.006552         12        640: 100% 16/16 [00:11<00:00,  1.42it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.21s/it]
                   all         70        166      0.896      0.831      0.875      0.568

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    197/999      12.9G      0.025    0.02323   0.006336         17        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.09s/it]
                   all         70        166       0.89      0.844      0.902      0.583

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    198/999      12.9G    0.02457    0.02294   0.005536         21        640: 100% 16/16 [00:10<00:00,  1.57it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.14it/s]
                   all         70        166      0.899      0.824      0.878      0.568

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    199/999      12.9G    0.02534    0.02305   0.005289         25        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:03<00:00,  3.32s/it]
                   all         70        166      0.873      0.848      0.893      0.597

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    200/999      12.9G    0.02427    0.02085   0.005758         19        640: 100% 16/16 [00:10<00:00,  1.58it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         70        166      0.947      0.877      0.931      0.622

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    201/999      12.9G    0.02452    0.02135   0.007186         14        640: 100% 16/16 [00:10<00:00,  1.47it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.30s/it]
                   all         70        166      0.925      0.885      0.935      0.629

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    202/999      12.9G    0.02419    0.02089   0.005775          7        640: 100% 16/16 [00:11<00:00,  1.35it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.79s/it]
                   all         70        166      0.898      0.839      0.903      0.587

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    203/999      12.9G     0.0261    0.02347   0.005249         51        640: 100% 16/16 [00:09<00:00,  1.60it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.12s/it]
                   all         70        166      0.892      0.812      0.905      0.591

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    204/999      12.9G     0.0253    0.02231   0.005487         19        640: 100% 16/16 [00:09<00:00,  1.64it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.01s/it]
                   all         70        166      0.893      0.821      0.894      0.574

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    205/999      12.9G    0.02437    0.02515   0.004786         49        640: 100% 16/16 [00:11<00:00,  1.42it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.08s/it]
                   all         70        166      0.909      0.785      0.887      0.585

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    206/999      12.9G    0.02451    0.02334   0.004934         11        640: 100% 16/16 [00:09<00:00,  1.69it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.23s/it]
                   all         70        166      0.893       0.81      0.871      0.567

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    207/999      12.9G    0.02453    0.02277   0.005095         25        640: 100% 16/16 [00:09<00:00,  1.63it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.22s/it]
                   all         70        166      0.885      0.877      0.897      0.618

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    208/999      12.9G    0.02482    0.02214    0.00904          7        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.15s/it]
                   all         70        166      0.904      0.837      0.904      0.629

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    209/999      12.9G    0.02519    0.02178   0.005855          9        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.10s/it]
                   all         70        166      0.907      0.808      0.892      0.586

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    210/999      12.9G     0.0241    0.02309   0.005596         27        640: 100% 16/16 [00:11<00:00,  1.40it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.10s/it]
                   all         70        166      0.887      0.834      0.884      0.595

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    211/999      12.9G    0.02432    0.02333   0.006014         39        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.24s/it]
                   all         70        166      0.893      0.824      0.866      0.574

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    212/999      12.9G    0.02672    0.02103   0.006275          7        640: 100% 16/16 [00:09<00:00,  1.69it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.22s/it]
                   all         70        166      0.901       0.87      0.901      0.601

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    213/999      12.9G    0.02545    0.02267   0.006275         18        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.24s/it]
                   all         70        166       0.89      0.835       0.91      0.618

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    214/999      12.9G    0.02374    0.02089   0.004795          4        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.25s/it]
                   all         70        166      0.879       0.83       0.88      0.599

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    215/999      12.9G    0.02336    0.02379   0.004227         30        640: 100% 16/16 [00:11<00:00,  1.42it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.13s/it]
                   all         70        166      0.915       0.85      0.908      0.618

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    216/999      12.9G    0.02488    0.02225   0.005211         12        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.28s/it]
                   all         70        166       0.88      0.869      0.911      0.607

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    217/999      12.9G    0.02412     0.0238   0.004045         74        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.15s/it]
                   all         70        166      0.905      0.783      0.882      0.591

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    218/999      12.9G    0.02322      0.025   0.004916         26        640: 100% 16/16 [00:09<00:00,  1.69it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.07s/it]
                   all         70        166      0.895      0.784      0.875      0.577

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    219/999      12.9G     0.0238    0.02122   0.004796         10        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.55s/it]
                   all         70        166      0.892      0.857      0.888      0.595

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    220/999      12.9G    0.02304    0.02075   0.004995         24        640: 100% 16/16 [00:10<00:00,  1.56it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.26s/it]
                   all         70        166      0.901      0.868      0.897      0.584

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    221/999      12.9G    0.02539    0.02149   0.005589         13        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.24s/it]
                   all         70        166      0.894      0.795      0.893      0.594

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    222/999      12.9G    0.02371    0.02314   0.004936         26        640: 100% 16/16 [00:09<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.03it/s]
                   all         70        166      0.902      0.842      0.909      0.612

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    223/999      12.9G    0.02329    0.02206   0.004454         27        640: 100% 16/16 [00:09<00:00,  1.60it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.06s/it]
                   all         70        166      0.888      0.865      0.907      0.617

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    224/999      12.9G     0.0239    0.02399   0.004829         32        640: 100% 16/16 [00:10<00:00,  1.48it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.37s/it]
                   all         70        166      0.907      0.857      0.916      0.614

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    225/999      12.9G    0.02364    0.02181   0.004665         14        640: 100% 16/16 [00:10<00:00,  1.56it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.14s/it]
                   all         70        166       0.87       0.86      0.889      0.615

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    226/999      12.9G    0.02542    0.02325   0.003918         28        640: 100% 16/16 [00:10<00:00,  1.59it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.09s/it]
                   all         70        166      0.909      0.865      0.908       0.61

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    227/999      12.9G    0.02323    0.02145   0.004652         14        640: 100% 16/16 [00:09<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.15s/it]
                   all         70        166      0.908      0.891      0.921      0.602

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    228/999      12.9G    0.02694    0.01973   0.007517          4        640: 100% 16/16 [00:09<00:00,  1.63it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.06s/it]
                   all         70        166       0.92      0.869      0.906      0.582

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    229/999      12.9G    0.02406    0.02194   0.005349         30        640: 100% 16/16 [00:13<00:00,  1.16it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.99s/it]
                   all         70        166       0.92      0.824      0.895      0.574

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    230/999      12.9G     0.0223    0.02005   0.005862         11        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.04s/it]
                   all         70        166      0.942      0.875      0.912      0.593

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    231/999      12.9G     0.0239    0.02121   0.006056         22        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.06s/it]
                   all         70        166      0.913      0.853      0.892      0.578

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    232/999      12.9G    0.02334    0.02257   0.004974          5        640: 100% 16/16 [00:09<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.18s/it]
                   all         70        166      0.914       0.85      0.895      0.582

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    233/999      12.9G    0.02405    0.02242   0.004796         15        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.55s/it]
                   all         70        166       0.89      0.829      0.899      0.586

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    234/999      12.9G    0.02353    0.02556   0.004514         84        640: 100% 16/16 [00:10<00:00,  1.53it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.10s/it]
                   all         70        166       0.93      0.873      0.927       0.61

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    235/999      12.9G    0.02305    0.02097   0.004477          6        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.14s/it]
                   all         70        166      0.936      0.877      0.923      0.602

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    236/999      12.9G    0.02344      0.021   0.006235         14        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.13s/it]
                   all         70        166      0.928      0.878       0.91      0.612

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    237/999      12.9G    0.02343    0.02227   0.006054          7        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.09s/it]
                   all         70        166      0.921      0.825       0.88      0.601

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    238/999      12.9G    0.02478    0.02051   0.005648         15        640: 100% 16/16 [00:10<00:00,  1.58it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.60s/it]
                   all         70        166      0.918      0.849      0.901      0.603

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    239/999      12.9G    0.02393    0.02024    0.00722          5        640: 100% 16/16 [00:09<00:00,  1.64it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.15s/it]
                   all         70        166      0.896      0.864      0.907      0.613

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    240/999      12.9G    0.02545    0.02059   0.008163         12        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.07s/it]
                   all         70        166      0.899      0.871      0.911       0.61

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    241/999      12.9G    0.02452    0.02175   0.004604         16        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.01it/s]
                   all         70        166      0.911      0.836      0.889      0.584

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    242/999      12.9G    0.02281    0.02314   0.005175          7        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.09s/it]
                   all         70        166      0.898      0.842      0.902      0.594

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    243/999      12.9G    0.02248    0.02175   0.004218          9        640: 100% 16/16 [00:10<00:00,  1.58it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.72s/it]
                   all         70        166      0.913      0.862      0.917      0.603

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    244/999      12.9G    0.02323    0.02198   0.003797          8        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.22s/it]
                   all         70        166       0.92      0.833      0.906      0.589

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    245/999      12.9G    0.02356     0.0229   0.004757         33        640: 100% 16/16 [00:09<00:00,  1.69it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.09s/it]
                   all         70        166      0.917      0.849      0.889       0.59

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    246/999      12.9G    0.02338      0.021   0.008707          6        640: 100% 16/16 [00:09<00:00,  1.70it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.15s/it]
                   all         70        166       0.91      0.826      0.884      0.591

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    247/999      12.9G    0.02354    0.02275   0.005062         34        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.04s/it]
                   all         70        166      0.905      0.836      0.896       0.58

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    248/999      12.9G    0.02309    0.01872   0.006083         12        640: 100% 16/16 [00:10<00:00,  1.47it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.40s/it]
                   all         70        166      0.892      0.816      0.886      0.584

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    249/999      12.9G    0.02328    0.02089    0.00436         32        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.14s/it]
                   all         70        166      0.924      0.813      0.896      0.581

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    250/999      12.9G    0.02268    0.02086   0.005513          9        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.15s/it]
                   all         70        166      0.922      0.841        0.9      0.595

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    251/999      12.9G    0.02513    0.02262   0.004782         11        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.07s/it]
                   all         70        166      0.866      0.831        0.9      0.597

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    252/999      12.9G    0.02296    0.02155   0.004813         22        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.03s/it]
                   all         70        166      0.874      0.882      0.893      0.582

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    253/999      12.9G    0.02247     0.0208   0.004999         12        640: 100% 16/16 [00:11<00:00,  1.44it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.29s/it]
                   all         70        166      0.878      0.864      0.882      0.582

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    254/999      12.9G    0.02326    0.02097   0.004308         17        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.02s/it]
                   all         70        166      0.911      0.843      0.899      0.581

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    255/999      12.9G      0.023    0.02078   0.005676          6        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.22s/it]
                   all         70        166      0.886      0.849      0.881      0.562

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    256/999      12.9G    0.02425    0.02156   0.005823         20        640: 100% 16/16 [00:09<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.18s/it]
                   all         70        166      0.895      0.827      0.891      0.595

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    257/999      12.9G    0.02366    0.02207   0.005565         30        640: 100% 16/16 [00:13<00:00,  1.21it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.68s/it]
                   all         70        166      0.918      0.834      0.892      0.587

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    258/999      12.9G     0.0238    0.02143   0.004539         17        640: 100% 16/16 [00:10<00:00,  1.57it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.03s/it]
                   all         70        166      0.911      0.803      0.876      0.584

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    259/999      12.9G    0.02213    0.02224   0.004761         13        640: 100% 16/16 [00:09<00:00,  1.64it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.06s/it]
                   all         70        166      0.905      0.816      0.879      0.592

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    260/999      12.9G    0.02276    0.02104   0.006222         31        640: 100% 16/16 [00:09<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.20s/it]
                   all         70        166      0.919      0.832      0.899       0.61

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    261/999      12.9G    0.02366    0.02352   0.004342         16        640: 100% 16/16 [00:09<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.07s/it]
                   all         70        166      0.923      0.877      0.914      0.616

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    262/999      12.9G     0.0241    0.02196   0.004814         34        640: 100% 16/16 [00:11<00:00,  1.43it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.27s/it]
                   all         70        166      0.917      0.892      0.924       0.63

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    263/999      12.9G    0.02412    0.02084   0.004386         11        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.24s/it]
                   all         70        166      0.905      0.866      0.914      0.617

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    264/999      12.9G    0.02373    0.02115   0.004591         22        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.05it/s]
                   all         70        166      0.874      0.842      0.891      0.602

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    265/999      12.9G      0.025    0.02248   0.006312         36        640: 100% 16/16 [00:09<00:00,  1.70it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.13s/it]
                   all         70        166      0.863      0.818      0.888      0.589

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    266/999      12.9G    0.02314    0.02323   0.005415         18        640: 100% 16/16 [00:09<00:00,  1.69it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.08s/it]
                   all         70        166      0.919      0.836      0.903      0.569

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    267/999      12.9G    0.02358    0.02196    0.00429          8        640: 100% 16/16 [00:11<00:00,  1.36it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.13s/it]
                   all         70        166      0.898      0.886      0.917      0.615

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    268/999      12.9G    0.02266    0.02018   0.005707         10        640: 100% 16/16 [00:09<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.21s/it]
                   all         70        166      0.927      0.895      0.927      0.625

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    269/999      12.9G    0.02261    0.01977   0.005682         17        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.08s/it]
                   all         70        166       0.93      0.865      0.926      0.618

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    270/999      12.9G    0.02187    0.02114   0.005006         27        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.07s/it]
                   all         70        166       0.89      0.867       0.91      0.608

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    271/999      12.9G     0.0235    0.02144   0.005409         11        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.06s/it]
                   all         70        166      0.922      0.847      0.889      0.601

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    272/999      12.9G    0.02392    0.02064   0.005055         16        640: 100% 16/16 [00:11<00:00,  1.37it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.12s/it]
                   all         70        166      0.907      0.839      0.886      0.594

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    273/999      12.9G    0.02369    0.02054   0.005887          7        640: 100% 16/16 [00:09<00:00,  1.69it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.12s/it]
                   all         70        166      0.936      0.825        0.9      0.608

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    274/999      12.9G    0.02378     0.0227   0.004371         13        640: 100% 16/16 [00:09<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.12s/it]
                   all         70        166      0.909      0.875      0.914      0.598

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    275/999      12.9G    0.02219    0.01991   0.005061          6        640: 100% 16/16 [00:09<00:00,  1.69it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.07s/it]
                   all         70        166      0.918      0.862       0.91      0.607

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    276/999      12.9G    0.02319    0.02122   0.004537         14        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         70        166       0.92      0.833      0.891      0.603

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    277/999      12.9G    0.02321    0.02146   0.005259          6        640: 100% 16/16 [00:11<00:00,  1.42it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.05s/it]
                   all         70        166      0.915       0.85      0.904      0.599

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    278/999      12.9G    0.02202    0.01903   0.005327         15        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.18s/it]
                   all         70        166      0.923      0.888       0.93      0.634

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    279/999      12.9G    0.02246    0.02169   0.004676         33        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.10s/it]
                   all         70        166      0.903      0.867      0.918      0.626

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    280/999      12.9G    0.02272    0.02081   0.005049         22        640: 100% 16/16 [00:09<00:00,  1.70it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.10s/it]
                   all         70        166      0.948      0.858      0.921      0.629

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    281/999      12.9G    0.02292    0.02065   0.005581         11        640: 100% 16/16 [00:09<00:00,  1.63it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.63s/it]
                   all         70        166      0.908      0.872      0.894      0.628

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    282/999      12.9G    0.02265    0.02085   0.004514         13        640: 100% 16/16 [00:10<00:00,  1.60it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.21s/it]
                   all         70        166      0.899      0.837      0.878      0.609

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    283/999      12.9G    0.02313    0.02084   0.004402         16        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.11s/it]
                   all         70        166       0.92       0.86      0.902      0.619

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    284/999      12.9G    0.02274    0.02074   0.004712         12        640: 100% 16/16 [00:11<00:00,  1.34it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.64s/it]
                   all         70        166        0.9      0.858      0.912        0.6

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    285/999      12.9G     0.0234    0.01892   0.006153         10        640: 100% 16/16 [00:09<00:00,  1.64it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.09s/it]
                   all         70        166      0.904      0.859      0.904      0.597

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    286/999      12.9G    0.02417    0.02076   0.006437         10        640: 100% 16/16 [00:11<00:00,  1.40it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.12s/it]
                   all         70        166      0.941      0.832      0.899      0.604

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    287/999      12.9G    0.02233    0.02269   0.004562         47        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.17s/it]
                   all         70        166      0.917      0.859      0.894      0.592

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    288/999      12.9G    0.02326    0.02015   0.004968         16        640: 100% 16/16 [00:09<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.17s/it]
                   all         70        166      0.911       0.87      0.898      0.606

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    289/999      12.9G     0.0218    0.02157   0.004686          1        640: 100% 16/16 [00:09<00:00,  1.64it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.01s/it]
                   all         70        166      0.886      0.844      0.893      0.601

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    290/999      12.9G    0.02369    0.01939   0.004758          7        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.01it/s]
                   all         70        166      0.916      0.836      0.892      0.595

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    291/999      12.9G    0.02216    0.02091   0.005099         26        640: 100% 16/16 [00:11<00:00,  1.41it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.24s/it]
                   all         70        166      0.918      0.866      0.908      0.625

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    292/999      12.9G    0.02214    0.02197   0.004813         39        640: 100% 16/16 [00:09<00:00,  1.73it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.14s/it]
                   all         70        166      0.898      0.853      0.893      0.593

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    293/999      12.9G     0.0228    0.02104   0.006002         14        640: 100% 16/16 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.21s/it]
                   all         70        166      0.908      0.854      0.893      0.577

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    294/999      12.9G    0.02232    0.02128   0.005536         25        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.10s/it]
                   all         70        166      0.901      0.849      0.888      0.584

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    295/999      12.9G    0.02172    0.01949   0.005941          7        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.35s/it]
                   all         70        166      0.898      0.855      0.896      0.594

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    296/999      12.9G    0.02349    0.01973   0.005203         18        640: 100% 16/16 [00:10<00:00,  1.50it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.00it/s]
                   all         70        166      0.923      0.828       0.89      0.597

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    297/999      12.9G    0.02449    0.01997    0.00513         11        640: 100% 16/16 [00:09<00:00,  1.72it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.14s/it]
                   all         70        166      0.911      0.858      0.885      0.599

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    298/999      12.9G    0.02366    0.02107   0.004769         37        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.22s/it]
                   all         70        166      0.902      0.846      0.898      0.595

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    299/999      12.9G    0.02249    0.02069   0.004107         31        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:03<00:00,  3.15s/it]
                   all         70        166       0.91      0.859      0.898      0.599

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    300/999      12.9G    0.02204    0.02049   0.006212         11        640: 100% 16/16 [00:11<00:00,  1.35it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.12s/it]
                   all         70        166      0.923      0.885      0.911      0.602

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    301/999      12.9G    0.02412     0.0207   0.004779         13        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.30s/it]
                   all         70        166      0.907      0.878      0.913        0.6

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    302/999      12.9G    0.02237    0.02006   0.005357         13        640: 100% 16/16 [00:09<00:00,  1.71it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.09s/it]
                   all         70        166      0.903       0.88      0.908       0.62

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    303/999      12.9G    0.02227    0.01903   0.006281          6        640: 100% 16/16 [00:09<00:00,  1.64it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.00s/it]
                   all         70        166      0.916      0.869      0.897      0.591

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    304/999      12.9G    0.02172    0.02047   0.005353         19        640: 100% 16/16 [00:09<00:00,  1.63it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.06s/it]
                   all         70        166      0.897      0.865      0.909      0.606

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    305/999      12.9G    0.02211    0.02027   0.004282          4        640: 100% 16/16 [00:11<00:00,  1.41it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.07it/s]
                   all         70        166      0.902      0.863      0.901      0.593

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    306/999      12.9G    0.02261    0.02002   0.003904         19        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.03s/it]
                   all         70        166      0.882      0.881      0.905      0.595

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    307/999      12.9G    0.02331    0.02065   0.005388         31        640: 100% 16/16 [00:09<00:00,  1.69it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.02s/it]
                   all         70        166      0.892      0.863      0.897        0.6

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    308/999      12.9G    0.02153    0.02008   0.004197          8        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.10s/it]
                   all         70        166      0.909      0.849      0.885      0.598

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    309/999      12.9G    0.02187     0.0193   0.005101          5        640: 100% 16/16 [00:09<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.59s/it]
                   all         70        166      0.895      0.877      0.896      0.609

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    310/999      12.9G    0.02337    0.02193   0.005056         10        640: 100% 16/16 [00:10<00:00,  1.52it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.08s/it]
                   all         70        166      0.934      0.832      0.894      0.609

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    311/999      12.9G    0.02205    0.02262   0.004495         38        640: 100% 16/16 [00:13<00:00,  1.23it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.10s/it]
                   all         70        166      0.915      0.849      0.893      0.597

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    312/999      12.9G    0.02495    0.02237   0.004285         93        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.16s/it]
                   all         70        166      0.888      0.883      0.914        0.6

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    313/999      12.9G    0.02158    0.02098   0.004007         29        640: 100% 16/16 [00:09<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.02s/it]
                   all         70        166      0.889      0.903      0.922      0.606

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    314/999      12.9G    0.02204    0.02149   0.004012          9        640: 100% 16/16 [00:11<00:00,  1.40it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.03s/it]
                   all         70        166      0.888      0.878      0.916      0.605

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    315/999      12.9G    0.02206    0.02014   0.004512          9        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.10s/it]
                   all         70        166      0.924      0.796      0.859      0.581

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    316/999      12.9G    0.02251    0.02152   0.004489         19        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.10s/it]
                   all         70        166      0.914      0.866      0.899      0.616

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    317/999      12.9G    0.02143    0.01961   0.005942         13        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.06s/it]
                   all         70        166      0.909      0.872      0.914      0.628

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    318/999      12.9G    0.02184    0.01978    0.00523          8        640: 100% 16/16 [00:09<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.06it/s]
                   all         70        166      0.882      0.907      0.925      0.629

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    319/999      12.9G    0.02184    0.02018   0.004789         22        640: 100% 16/16 [00:11<00:00,  1.36it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.00it/s]
                   all         70        166      0.948       0.87      0.928      0.624

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    320/999      12.9G    0.02236    0.02084   0.004955         38        640: 100% 16/16 [00:09<00:00,  1.70it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.09s/it]
                   all         70        166      0.946       0.88      0.928      0.631

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    321/999      12.9G    0.02202     0.0193   0.005086         12        640: 100% 16/16 [00:09<00:00,  1.63it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.02s/it]
                   all         70        166      0.911      0.866       0.92      0.617

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    322/999      12.9G    0.02189    0.02178   0.004407         48        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.24s/it]
                   all         70        166      0.863      0.904      0.926      0.613

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    323/999      12.9G    0.02188    0.02005   0.004414         10        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.68s/it]
                   all         70        166      0.854      0.912      0.922      0.622

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    324/999      12.9G    0.02235    0.02052   0.004219         13        640: 100% 16/16 [00:10<00:00,  1.51it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.09s/it]
                   all         70        166      0.925      0.838      0.909      0.612

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    325/999      12.9G    0.02239     0.0211   0.004992         33        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.11s/it]
                   all         70        166      0.911      0.845      0.896      0.606

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    326/999      12.9G    0.02291    0.02299   0.004188         74        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.09s/it]
                   all         70        166      0.914      0.833      0.908      0.601

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    327/999      12.9G    0.02165    0.01831   0.007759         15        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.09s/it]
                   all         70        166      0.881       0.86      0.909      0.603

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    328/999      12.9G    0.02115    0.01729   0.004875          7        640: 100% 16/16 [00:10<00:00,  1.47it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.25s/it]
                   all         70        166      0.924      0.835      0.906      0.592

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    329/999      12.9G    0.02287    0.02062   0.005362         28        640: 100% 16/16 [00:09<00:00,  1.64it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.11s/it]
                   all         70        166      0.923      0.862      0.903      0.588

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    330/999      12.9G    0.02316    0.02247    0.00375         22        640: 100% 16/16 [00:09<00:00,  1.69it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.10s/it]
                   all         70        166      0.911      0.864      0.908      0.604

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    331/999      12.9G     0.0231     0.0186   0.005117         11        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.04s/it]
                   all         70        166      0.904       0.85      0.908      0.607

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    332/999      12.9G    0.02176    0.01929   0.005193         20        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.08s/it]
                   all         70        166      0.928      0.815        0.9      0.601

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    333/999      12.9G    0.02321    0.02006   0.005241         12        640: 100% 16/16 [00:11<00:00,  1.44it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.12s/it]
                   all         70        166      0.915      0.875      0.908      0.615

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    334/999      12.9G     0.0216    0.01995    0.00515         16        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.05it/s]
                   all         70        166      0.921      0.862      0.912       0.62

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    335/999      12.9G    0.02233    0.01913   0.004024          9        640: 100% 16/16 [00:09<00:00,  1.63it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.03it/s]
                   all         70        166      0.923      0.804      0.886      0.596

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    336/999      12.9G    0.02136    0.02013   0.004391         36        640: 100% 16/16 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.06s/it]
                   all         70        166      0.935      0.814      0.899      0.613

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    337/999      12.9G    0.02142    0.01969   0.005547         19        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.22s/it]
                   all         70        166       0.93      0.863      0.906      0.614

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    338/999      12.9G    0.02166    0.02107   0.004722         29        640: 100% 16/16 [00:14<00:00,  1.09it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.15s/it]
                   all         70        166      0.927      0.873      0.918      0.624

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    339/999      12.9G    0.02258    0.02266   0.006065         27        640: 100% 16/16 [00:09<00:00,  1.64it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.12s/it]
                   all         70        166      0.921      0.894      0.911      0.614

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    340/999      12.9G    0.02224    0.01974   0.004408         12        640: 100% 16/16 [00:09<00:00,  1.69it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.21s/it]
                   all         70        166      0.932      0.859        0.9      0.612

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    341/999      12.9G    0.02198    0.02018   0.005119          7        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.01s/it]
                   all         70        166      0.905       0.87      0.899      0.603

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    342/999      12.9G    0.02138    0.02118   0.005464         43        640: 100% 16/16 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.61s/it]
                   all         70        166      0.914      0.859      0.889      0.602

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    343/999      12.9G    0.02348    0.02306   0.004187         58        640: 100% 16/16 [00:10<00:00,  1.59it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.03s/it]
                   all         70        166      0.912      0.852      0.894      0.601

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    344/999      12.9G    0.02214    0.02105   0.005503          8        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         70        166      0.948      0.839      0.902      0.613

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    345/999      12.9G    0.02224    0.02092   0.004394         34        640: 100% 16/16 [00:09<00:00,  1.63it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.08s/it]
                   all         70        166       0.95      0.825      0.899      0.606

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    346/999      12.9G    0.02169    0.01825   0.007623         12        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.21s/it]
                   all         70        166      0.893       0.84      0.903      0.603

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    347/999      12.9G    0.02214    0.02049   0.004582         24        640: 100% 16/16 [00:11<00:00,  1.43it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.02s/it]
                   all         70        166      0.908      0.831       0.91      0.616

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    348/999      12.9G    0.02259    0.01969   0.004311         44        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.16s/it]
                   all         70        166      0.937      0.853      0.919      0.629

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    349/999      12.9G     0.0224    0.01992   0.005884          4        640: 100% 16/16 [00:09<00:00,  1.62it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.17s/it]
                   all         70        166      0.938      0.881      0.917      0.628

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    350/999      12.9G    0.02152    0.01967    0.00437         13        640: 100% 16/16 [00:09<00:00,  1.60it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.17s/it]
                   all         70        166      0.962      0.847      0.905      0.617

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    351/999      12.9G     0.0216    0.01957   0.004944         11        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.26s/it]
                   all         70        166      0.935      0.853      0.899      0.613

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    352/999      12.9G    0.02172    0.02153   0.004545         26        640: 100% 16/16 [00:11<00:00,  1.43it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.16s/it]
                   all         70        166      0.892      0.864      0.903      0.611

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    353/999      12.9G     0.0206    0.02278   0.004789         46        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.09s/it]
                   all         70        166      0.899      0.843      0.905      0.612

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    354/999      12.9G    0.02135    0.01827    0.00576         10        640: 100% 16/16 [00:09<00:00,  1.70it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.09s/it]
                   all         70        166      0.909      0.853      0.909      0.608

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    355/999      12.9G    0.02037    0.01899   0.004882         11        640: 100% 16/16 [00:09<00:00,  1.63it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.03s/it]
                   all         70        166      0.935      0.894      0.934      0.631

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    356/999      12.9G    0.02312    0.02269   0.006484         45        640: 100% 16/16 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         70        166      0.912      0.911      0.937      0.632

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    357/999      12.9G    0.02195    0.02073   0.005764          6        640: 100% 16/16 [00:11<00:00,  1.40it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.26s/it]
                   all         70        166      0.929      0.896      0.931      0.629

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    358/999      12.9G    0.02154    0.02064   0.006566          6        640: 100% 16/16 [00:09<00:00,  1.63it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.11s/it]
                   all         70        166      0.936       0.88      0.922      0.622

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    359/999      12.9G      0.022    0.01975   0.004993         14        640: 100% 16/16 [00:09<00:00,  1.63it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.12s/it]
                   all         70        166      0.896      0.846      0.887      0.593

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    360/999      12.9G    0.02346    0.01816   0.005862          5        640: 100% 16/16 [00:09<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.11s/it]
                   all         70        166      0.896      0.837      0.882      0.594

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    361/999      12.9G    0.02244    0.02006   0.005587         13        640: 100% 16/16 [00:10<00:00,  1.53it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.45s/it]
                   all         70        166      0.899      0.822      0.887        0.6

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    362/999      12.9G    0.02129    0.01905   0.004681          9        640: 100% 16/16 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.17s/it]
                   all         70        166      0.931        0.8       0.89      0.606

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    363/999      12.9G    0.02164    0.02127    0.00469         38        640: 100% 16/16 [00:09<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.15it/s]
                   all         70        166      0.916      0.826      0.893      0.615

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    364/999      12.9G     0.0219    0.02084   0.004773         16        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.17s/it]
                   all         70        166      0.915      0.842      0.899      0.613

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    365/999      12.9G    0.02165    0.01835   0.005488         21        640: 100% 16/16 [00:11<00:00,  1.37it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.56s/it]
                   all         70        166      0.928      0.834      0.906      0.611

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    366/999      12.9G    0.02253     0.0192   0.004449         19        640: 100% 16/16 [00:12<00:00,  1.31it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.07s/it]
                   all         70        166      0.946      0.837      0.904      0.618

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    367/999      12.9G    0.02143    0.01933    0.00524         18        640: 100% 16/16 [00:09<00:00,  1.64it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.03it/s]
                   all         70        166      0.951      0.831      0.896      0.605

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    368/999      12.9G    0.02293    0.02077   0.004339         38        640: 100% 16/16 [00:09<00:00,  1.64it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.06s/it]
                   all         70        166      0.929      0.839      0.906      0.613

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    369/999      12.9G    0.02042    0.02019   0.004199         37        640: 100% 16/16 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.03it/s]
                   all         70        166      0.923      0.817      0.901      0.605

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    370/999      12.9G    0.02097    0.02093   0.005891         13        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.00it/s]
                   all         70        166      0.942       0.87      0.906       0.61

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    371/999      12.9G    0.02345    0.02102    0.00512         42        640: 100% 16/16 [00:11<00:00,  1.39it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.13s/it]
                   all         70        166      0.933      0.843      0.911      0.608

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    372/999      12.9G    0.02149    0.01998   0.005259         20        640: 100% 16/16 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.07s/it]
                   all         70        166      0.927      0.817      0.904      0.608

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    373/999      12.9G    0.02112    0.02018   0.005062         17        640: 100% 16/16 [00:09<00:00,  1.69it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.01s/it]
                   all         70        166      0.911      0.853      0.907      0.611

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    374/999      12.9G    0.02245    0.02053   0.004961         16        640: 100% 16/16 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.05s/it]
                   all         70        166       0.95       0.89      0.924       0.62

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    375/999      12.9G    0.02269    0.02196   0.004525         67        640: 100% 16/16 [00:09<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.64s/it]
                   all         70        166      0.954      0.901      0.929      0.622

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    376/999      12.9G    0.02195    0.02098   0.004729          8        640: 100% 16/16 [00:10<00:00,  1.49it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.06s/it]
                   all         70        166      0.929       0.88      0.927      0.628

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    377/999      12.9G    0.02115    0.01891   0.004676         14        640: 100% 16/16 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.03s/it]
                   all         70        166      0.932      0.856      0.912      0.616

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    378/999      12.9G    0.02023    0.01936   0.004717          8        640: 100% 16/16 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.15s/it]
                   all         70        166      0.936      0.845      0.909      0.606
Stopping training early as no improvement observed in last 100 epochs. Best results observed at epoch 278, best model saved as best.pt.
To update EarlyStopping(patience=100) pass a new patience value, i.e. `python train.py --patience 300` or use `--patience 0` to disable EarlyStopping.

379 epochs completed in 1.294 hours.
Optimizer stripped from runs/train/exp2/weights/last.pt, 14.5MB
Optimizer stripped from runs/train/exp2/weights/best.pt, 14.5MB

Validating runs/train/exp2/weights/best.pt...
Fusing layers... 
Model summary: 157 layers, 7018216 parameters, 0 gradients, 15.8 GFLOPs
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.23it/s]
                   all         70        166      0.923      0.888       0.93      0.633
             amaciante         70         37      0.944      0.916      0.955      0.644
                 aveia         70         65      0.925      0.908      0.947      0.677
               shampoo         70         64        0.9      0.839      0.888      0.579
  ```
</details>

### Evidências do treinamento

![Gráficos de Perdas](https://api.wandb.ai/files/camilacorreamelo/YOLOv5/1djfl4w4/media/images/Results_379_3f995a9cdaa25aa2188d.png?height=255)
![Matriz de Confusão](https://api.wandb.ai/files/camilacorreamelo/YOLOv5/1djfl4w4/media/images/Results_379_8e08f13dbe0e961fe139.png?height=255)

## Roboflow

[/especializacao/supermarket](https://universe.roboflow.com/especializao/supermarket-oqn4b)

## HuggingFace

Nessa seção você deve publicar o link para o HuggingFace