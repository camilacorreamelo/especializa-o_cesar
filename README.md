# Projeto Final - Modelos Preditivos Conexionistas

### CAMILA CORRÊA DE MELO

|**DETECCAO**|**YOLOv5**|**PyTorch**|


## Purpose

This project aims to create a model to detect different surgery instruments. It considered three instrument classes: scalpel, needle holder and farabeuf retractor, sice they are main instruments used by physicians. 

## Performance

O modelo treinado possui performance de **73.7%**.

### Output do bloco de treinamento

<details>
  <summary>Click to expand!</summary>
  
  ``` Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      0/499      10.2G     0.1095    0.03323     0.0419         26        640: 100% 15/15 [00:12<00:00,  1.22it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:02<00:00,  2.45s/it]
                   all         51         87     0.0027      0.469     0.0237    0.00587

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      1/499      10.2G    0.08632    0.03235    0.03949         23        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.11s/it]
                   all         51         87     0.0569      0.023     0.0474     0.0197

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      2/499      10.2G    0.07104    0.03228    0.03629         31        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.03it/s]
                   all         51         87     0.0966      0.331      0.127     0.0617

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      3/499      10.2G    0.06265    0.02821    0.03438         19        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.02it/s]
                   all         51         87      0.228      0.239       0.21      0.107

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      4/499      10.2G    0.05609    0.02516    0.03257         11        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.12it/s]
                   all         51         87      0.133      0.223      0.127     0.0668

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      5/499      10.2G     0.0549    0.02468     0.0315         17        640: 100% 15/15 [00:08<00:00,  1.83it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.14it/s]
                   all         51         87      0.107      0.277     0.0941     0.0393

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      6/499      10.2G     0.0543    0.02673    0.02989         31        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.06it/s]
                   all         51         87      0.186      0.415      0.159     0.0724

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      7/499      10.2G    0.05053    0.02461    0.02979         21        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.01it/s]
                   all         51         87     0.0994      0.332      0.124     0.0538

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      8/499      10.2G    0.04862    0.02395    0.03023         12        640: 100% 15/15 [00:08<00:00,  1.83it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.04s/it]
                   all         51         87     0.0754      0.142     0.0618     0.0271

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
      9/499      10.2G    0.04787      0.025    0.02953         20        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.29it/s]
                   all         51         87     0.0418     0.0541    0.00894    0.00431

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     10/499      10.2G    0.04552    0.02381    0.02698         19        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.16it/s]
                   all         51         87     0.0129      0.131    0.00719     0.0027

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     11/499      10.2G    0.04683     0.0232    0.02665         20        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.10s/it]
                   all         51         87     0.0311       0.16       0.04     0.0154

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     12/499      10.2G    0.04548    0.02299    0.02813         22        640: 100% 15/15 [00:08<00:00,  1.81it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.18it/s]
                   all         51         87       0.27      0.389      0.207      0.105

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     13/499      10.2G    0.04572    0.02368    0.02938         33        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.35it/s]
                   all         51         87      0.327      0.394      0.247      0.142

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     14/499      10.2G    0.04512    0.02124    0.02732         25        640: 100% 15/15 [00:08<00:00,  1.83it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.33it/s]
                   all         51         87      0.344      0.355      0.275      0.139

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     15/499      10.2G    0.04541    0.02341    0.02636         16        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.16it/s]
                   all         51         87      0.351      0.517      0.322      0.187

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     16/499      10.2G    0.04319    0.02288    0.02806         17        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.12it/s]
                   all         51         87      0.429       0.49      0.328      0.175

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     17/499      10.2G    0.04284     0.0226    0.02655         26        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.02it/s]
                   all         51         87      0.235       0.31      0.198     0.0778

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     18/499      10.2G    0.04491    0.02338    0.02636         41        640: 100% 15/15 [00:08<00:00,  1.71it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.34s/it]
                   all         51         87      0.254      0.384      0.172      0.069

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     19/499      10.2G    0.04115    0.02097    0.02846         17        640: 100% 15/15 [00:09<00:00,  1.56it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.04it/s]
                   all         51         87      0.324      0.441      0.289       0.14

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     20/499      10.2G    0.04243    0.02274    0.02601         32        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.07it/s]
                   all         51         87      0.444      0.347      0.302      0.167

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     21/499      10.2G    0.04211    0.02102    0.02505         15        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.04it/s]
                   all         51         87      0.508      0.435      0.387      0.231

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     22/499      10.2G    0.04191    0.02182    0.02477         24        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.05it/s]
                   all         51         87      0.622      0.455      0.426      0.208

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     23/499      10.2G    0.03986     0.0216    0.02444         25        640: 100% 15/15 [00:08<00:00,  1.71it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.11it/s]
                   all         51         87      0.574      0.419      0.388      0.227

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     24/499      10.2G    0.04211    0.02143    0.02451         26        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.19it/s]
                   all         51         87      0.651      0.535      0.538      0.322

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     25/499      10.2G    0.04122    0.02108    0.02575         24        640: 100% 15/15 [00:08<00:00,  1.81it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.23it/s]
                   all         51         87       0.59      0.441      0.392      0.188

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     26/499      10.2G    0.04186     0.0205    0.02502         17        640: 100% 15/15 [00:08<00:00,  1.82it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.03s/it]
                   all         51         87        0.6      0.469      0.482      0.283

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     27/499      10.2G    0.03894    0.02088    0.02614         20        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.14it/s]
                   all         51         87      0.405      0.469      0.388      0.193

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     28/499      10.2G    0.03946    0.02147    0.02399         26        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.02it/s]
                   all         51         87       0.47      0.544      0.443      0.262

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     29/499      10.2G    0.04054    0.02026    0.02338         17        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.09it/s]
                   all         51         87       0.54      0.397      0.428      0.233

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     30/499      10.2G    0.03991    0.02144    0.02081         28        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.16it/s]
                   all         51         87      0.613      0.487      0.506       0.29

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     31/499      10.2G    0.03987    0.02004    0.02293         15        640: 100% 15/15 [00:08<00:00,  1.69it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.31it/s]
                   all         51         87      0.406      0.445       0.36      0.211

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     32/499      10.2G    0.04195    0.02028    0.02306         28        640: 100% 15/15 [00:08<00:00,  1.73it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.08it/s]
                   all         51         87       0.42      0.428      0.369       0.19

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     33/499      10.2G     0.0409    0.01933    0.02273         14        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.21it/s]
                   all         51         87      0.308      0.325      0.264      0.144

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     34/499      10.2G    0.03856    0.02023    0.02342         13        640: 100% 15/15 [00:08<00:00,  1.74it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.15it/s]
                   all         51         87      0.559      0.382      0.416      0.249

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     35/499      10.2G    0.03751    0.02027    0.02175         29        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.25it/s]
                   all         51         87      0.342      0.494      0.329      0.145

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     36/499      10.2G    0.03867    0.02075    0.02262         24        640: 100% 15/15 [00:08<00:00,  1.71it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.63s/it]
                   all         51         87      0.449      0.549      0.429      0.218

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     37/499      10.2G      0.039    0.02037    0.02377         23        640: 100% 15/15 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.12it/s]
                   all         51         87       0.62      0.442      0.464      0.273

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     38/499      10.2G    0.03831    0.01949    0.02208         15        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.10it/s]
                   all         51         87      0.572      0.559      0.537      0.303

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     39/499      10.2G    0.03766    0.01905     0.0224         12        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.01s/it]
                   all         51         87      0.637      0.561      0.522      0.302

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     40/499      10.2G    0.03628     0.0186    0.02358         11        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.24it/s]
                   all         51         87      0.532      0.507      0.411      0.265

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     41/499      10.2G    0.03739    0.01831    0.02343         13        640: 100% 15/15 [00:08<00:00,  1.82it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.14it/s]
                   all         51         87      0.555      0.499      0.426      0.272

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     42/499      10.2G     0.0381     0.0195    0.02329         21        640: 100% 15/15 [00:08<00:00,  1.82it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.21it/s]
                   all         51         87      0.386      0.468      0.352      0.191

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     43/499      10.2G    0.03888    0.01939      0.022         30        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.04s/it]
                   all         51         87      0.603      0.458      0.473      0.272

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     44/499      10.2G    0.03668    0.01899    0.02308         14        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.02it/s]
                   all         51         87      0.514      0.596       0.47      0.294

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     45/499      10.2G    0.03731    0.01889    0.02447         16        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.21it/s]
                   all         51         87      0.538       0.58      0.468      0.275

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     46/499      10.2G    0.03925    0.01881    0.02272         22        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.07it/s]
                   all         51         87       0.55      0.541      0.478      0.289

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     47/499      10.2G    0.03769    0.01939    0.02383         29        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.00it/s]
                   all         51         87      0.642      0.477      0.504      0.305

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     48/499      10.2G    0.03673    0.01857    0.02155         32        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.25it/s]
                   all         51         87      0.393      0.495      0.403      0.252

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     49/499      10.2G    0.03784    0.01927    0.02302         19        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:02<00:00,  2.85s/it]
                   all         51         87      0.622      0.532      0.487      0.279

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     50/499      10.2G    0.03744    0.01885    0.02213         16        640: 100% 15/15 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.08it/s]
                   all         51         87      0.659       0.49      0.507      0.305

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     51/499      10.2G    0.03808    0.01791    0.02199         16        640: 100% 15/15 [00:08<00:00,  1.81it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.38it/s]
                   all         51         87      0.433      0.509      0.443      0.257

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     52/499      10.2G    0.03811     0.0193     0.0217         14        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.06it/s]
                   all         51         87       0.52      0.571      0.496      0.317

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     53/499      10.2G    0.03715    0.01851     0.0222         21        640: 100% 15/15 [00:08<00:00,  1.81it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.27it/s]
                   all         51         87      0.413      0.596      0.496      0.295

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     54/499      10.2G    0.03577    0.01754    0.02214         15        640: 100% 15/15 [00:10<00:00,  1.50it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.30s/it]
                   all         51         87      0.431      0.512      0.408      0.225

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     55/499      10.2G    0.03624    0.01912     0.0228         23        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.14it/s]
                   all         51         87      0.714      0.484      0.514      0.331

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     56/499      10.2G    0.03633    0.01752      0.022         19        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.19it/s]
                   all         51         87      0.635      0.507      0.514      0.278

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     57/499      10.2G    0.03501    0.01888    0.02208         36        640: 100% 15/15 [00:08<00:00,  1.83it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.04it/s]
                   all         51         87      0.533      0.536      0.487      0.321

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     58/499      10.2G    0.03626    0.01886    0.02088         22        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.15it/s]
                   all         51         87      0.657      0.494      0.519      0.345

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     59/499      10.2G    0.03583    0.01824     0.0228         14        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.11it/s]
                   all         51         87       0.54      0.505      0.493      0.302

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     60/499      10.2G    0.03431    0.01832     0.0223         20        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.26it/s]
                   all         51         87      0.591      0.515      0.537      0.332

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     61/499      10.2G    0.03629    0.01834    0.02178         17        640: 100% 15/15 [00:08<00:00,  1.70it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.17it/s]
                   all         51         87      0.481      0.539      0.478      0.309

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     62/499      10.2G    0.03643    0.01791    0.02326         15        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.07it/s]
                   all         51         87      0.551      0.521      0.489      0.317

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     63/499      10.2G    0.03466    0.01761    0.02026         21        640: 100% 15/15 [00:08<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.30it/s]
                   all         51         87      0.603      0.493      0.516      0.317

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     64/499      10.2G    0.03652    0.01829    0.02197         22        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.22it/s]
                   all         51         87      0.506        0.5      0.437       0.23

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     65/499      10.2G    0.03658    0.01783    0.02105         14        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.18it/s]
                   all         51         87      0.446      0.473      0.376      0.232

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     66/499      10.2G    0.03596     0.0178     0.0222         10        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.02it/s]
                   all         51         87      0.638      0.544      0.491      0.306

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     67/499      10.2G    0.03525    0.01868    0.02119         18        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.38it/s]
                   all         51         87      0.659      0.512      0.559      0.369

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     68/499      10.2G    0.03536    0.01774    0.02216         22        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.15it/s]
                   all         51         87       0.49      0.432       0.41      0.227

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     69/499      10.2G    0.03452    0.01843    0.02323         21        640: 100% 15/15 [00:08<00:00,  1.81it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.24it/s]
                   all         51         87       0.59      0.526      0.471      0.286

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     70/499      10.2G    0.03315    0.01832    0.02117          7        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.01it/s]
                   all         51         87       0.42      0.507      0.412      0.265

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     71/499      10.2G    0.03442    0.01733    0.02401         12        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.18it/s]
                   all         51         87       0.49      0.485      0.412      0.266

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     72/499      10.2G    0.03607    0.01814    0.02052         18        640: 100% 15/15 [00:10<00:00,  1.38it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.21it/s]
                   all         51         87      0.543      0.537       0.42      0.273

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     73/499      10.2G    0.03375    0.01793    0.02189         19        640: 100% 15/15 [00:08<00:00,  1.73it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.16it/s]
                   all         51         87      0.546      0.596      0.521      0.344

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     74/499      10.2G     0.0331    0.01709    0.02056         23        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.15it/s]
                   all         51         87      0.624      0.584      0.522       0.33

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     75/499      10.2G    0.03342    0.01714    0.02355         19        640: 100% 15/15 [00:08<00:00,  1.71it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.33it/s]
                   all         51         87      0.391      0.443      0.407       0.26

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     76/499      10.2G    0.03375     0.0167    0.02167         18        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.32it/s]
                   all         51         87      0.582      0.522       0.45      0.281

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     77/499      10.2G    0.03233    0.01779    0.02103         26        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.08it/s]
                   all         51         87      0.451      0.496      0.386      0.248

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     78/499      10.2G    0.03437    0.01758     0.0214         24        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.17it/s]
                   all         51         87      0.694      0.545      0.508      0.328

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     79/499      10.2G    0.03438    0.01711    0.02086         24        640: 100% 15/15 [00:08<00:00,  1.73it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.40it/s]
                   all         51         87      0.555      0.525      0.487       0.31

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     80/499      10.2G    0.03471    0.01802    0.02285         15        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.11it/s]
                   all         51         87      0.526      0.454      0.417      0.255

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     81/499      10.2G      0.033    0.01768    0.02205         18        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.26it/s]
                   all         51         87      0.427      0.392       0.35      0.202

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     82/499      10.2G    0.03602    0.01768    0.02071         14        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.10it/s]
                   all         51         87      0.775       0.51       0.55      0.324

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     83/499      10.2G    0.03343    0.01673    0.02122         23        640: 100% 15/15 [00:08<00:00,  1.81it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.25it/s]
                   all         51         87      0.583      0.603      0.498       0.31

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     84/499      10.2G    0.03388    0.01676    0.02159         21        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.26it/s]
                   all         51         87      0.492      0.476      0.401      0.227

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     85/499      10.2G    0.03411    0.01874    0.02097         43        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.27it/s]
                   all         51         87      0.646      0.475       0.51      0.321

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     86/499      10.2G    0.03391     0.0174    0.02128         20        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.36it/s]
                   all         51         87      0.503      0.504       0.42      0.249

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     87/499      10.2G    0.03263    0.01794    0.02103         29        640: 100% 15/15 [00:08<00:00,  1.74it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.10it/s]
                   all         51         87      0.524      0.538       0.48      0.325

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     88/499      10.2G    0.03319    0.01714    0.02148         22        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.04it/s]
                   all         51         87      0.613      0.547      0.449      0.282

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     89/499      10.2G    0.03174    0.01682    0.01961         14        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.14it/s]
                   all         51         87      0.544      0.612      0.487      0.307

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     90/499      10.2G    0.03401    0.01779    0.02241         23        640: 100% 15/15 [00:10<00:00,  1.44it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.19s/it]
                   all         51         87      0.673       0.48      0.518       0.34

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     91/499      10.2G     0.0332    0.01766    0.02071         24        640: 100% 15/15 [00:09<00:00,  1.66it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.44it/s]
                   all         51         87      0.435      0.541      0.459      0.273

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     92/499      10.2G     0.0341    0.01775    0.02212         20        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.27it/s]
                   all         51         87      0.549       0.51      0.521      0.337

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     93/499      10.2G    0.03314    0.01666      0.021         18        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.10it/s]
                   all         51         87      0.544      0.536      0.475      0.281

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     94/499      10.2G    0.03176    0.01746    0.02015         15        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.05it/s]
                   all         51         87       0.56      0.512      0.497      0.292

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     95/499      10.2G    0.03131    0.01714    0.02029         14        640: 100% 15/15 [00:08<00:00,  1.73it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.17it/s]
                   all         51         87      0.572       0.47      0.525      0.334

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     96/499      10.2G    0.03222    0.01676    0.01951         19        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.14it/s]
                   all         51         87      0.593      0.565      0.479      0.298

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     97/499      10.2G    0.03255    0.01722    0.01783         23        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.07it/s]
                   all         51         87      0.678      0.566      0.577      0.415

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     98/499      10.2G    0.03295    0.01569    0.01791         11        640: 100% 15/15 [00:08<00:00,  1.81it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.17it/s]
                   all         51         87      0.558      0.468      0.409       0.24

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
     99/499      10.2G    0.03217    0.01659    0.01966         19        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:02<00:00,  2.79s/it]
                   all         51         87      0.587      0.572      0.489      0.314

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    100/499      10.2G     0.0336    0.01707    0.02122         22        640: 100% 15/15 [00:08<00:00,  1.71it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.12it/s]
                   all         51         87      0.362       0.39      0.347      0.177

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    101/499      10.2G    0.03193    0.01657    0.01878         22        640: 100% 15/15 [00:08<00:00,  1.69it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.17it/s]
                   all         51         87      0.444       0.49      0.414      0.283

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    102/499      10.2G    0.03321    0.01666    0.01977         22        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.04it/s]
                   all         51         87      0.512       0.43      0.385      0.263

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    103/499      10.2G    0.03259    0.01668    0.02021         18        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.29it/s]
                   all         51         87      0.516      0.488      0.429      0.291

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    104/499      10.2G    0.03303    0.01668    0.01996         16        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.05it/s]
                   all         51         87      0.642      0.546      0.517       0.36

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    105/499      10.2G     0.0316    0.01694    0.02077         20        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.18it/s]
                   all         51         87       0.63       0.56      0.513      0.359

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    106/499      10.2G    0.03113    0.01622    0.02095         14        640: 100% 15/15 [00:08<00:00,  1.81it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.24it/s]
                   all         51         87      0.664      0.593      0.525       0.36

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    107/499      10.2G    0.03341    0.01633    0.01893         29        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.13it/s]
                   all         51         87      0.742       0.59      0.586      0.401

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    108/499      10.2G    0.03302    0.01743    0.01895         35        640: 100% 15/15 [00:10<00:00,  1.39it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.08it/s]
                   all         51         87       0.74      0.551      0.564      0.374

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    109/499      10.2G    0.03118     0.0162    0.02032         18        640: 100% 15/15 [00:08<00:00,  1.74it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.18it/s]
                   all         51         87      0.658      0.546      0.567      0.364

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    110/499      10.2G    0.03185    0.01611    0.02318         15        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.13it/s]
                   all         51         87      0.637      0.449      0.494       0.32

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    111/499      10.2G    0.03257    0.01664    0.02032         25        640: 100% 15/15 [00:08<00:00,  1.71it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.19it/s]
                   all         51         87       0.61      0.424      0.463      0.287

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    112/499      10.2G    0.03227    0.01701    0.02011         18        640: 100% 15/15 [00:08<00:00,  1.74it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.17it/s]
                   all         51         87      0.469      0.496      0.459      0.293

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    113/499      10.2G    0.03252     0.0155    0.02131          9        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.20it/s]
                   all         51         87      0.647      0.572       0.55      0.344

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    114/499      10.2G    0.03192    0.01748    0.02146         25        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.32it/s]
                   all         51         87      0.492      0.535      0.504       0.33

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    115/499      10.2G    0.03221    0.01689    0.02126         27        640: 100% 15/15 [00:08<00:00,  1.83it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.18it/s]
                   all         51         87      0.418      0.535      0.363       0.22

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    116/499      10.2G     0.0338    0.01693    0.01881         18        640: 100% 15/15 [00:08<00:00,  1.72it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.09it/s]
                   all         51         87      0.551      0.492      0.459       0.28

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    117/499      10.2G    0.03122    0.01574    0.02324         16        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.09it/s]
                   all         51         87      0.525       0.53      0.452      0.267

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    118/499      10.2G     0.0307    0.01637    0.02244         15        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.16it/s]
                   all         51         87      0.601      0.568      0.527      0.335

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    119/499      10.2G    0.03346    0.01599     0.0208         16        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.13it/s]
                   all         51         87      0.606      0.518      0.484      0.328

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    120/499      10.2G    0.03049    0.01739    0.01944         30        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.27it/s]
                   all         51         87      0.605      0.477      0.494      0.317

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    121/499      10.2G    0.03142    0.01555    0.02095         15        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.15it/s]
                   all         51         87      0.582      0.541      0.491      0.321

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    122/499      10.2G    0.03241    0.01548    0.02006         20        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.03it/s]
                   all         51         87      0.541        0.6      0.502      0.338

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    123/499      10.2G    0.03186    0.01656    0.01964         22        640: 100% 15/15 [00:08<00:00,  1.73it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.22it/s]
                   all         51         87      0.579      0.521      0.496      0.347

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    124/499      10.2G    0.03183    0.01676    0.01838         28        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.18it/s]
                   all         51         87      0.531      0.379      0.393      0.256

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    125/499      10.2G    0.03239    0.01732    0.01941         29        640: 100% 15/15 [00:08<00:00,  1.70it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.32s/it]
                   all         51         87      0.525      0.435      0.416       0.27

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    126/499      10.2G     0.0319    0.01762    0.01932         30        640: 100% 15/15 [00:09<00:00,  1.58it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.02it/s]
                   all         51         87      0.479      0.523      0.425      0.289

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    127/499      10.2G    0.03256    0.01632    0.01967         13        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.02s/it]
                   all         51         87      0.622      0.423      0.454      0.299

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    128/499      10.2G    0.03104    0.01592    0.01978         21        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.25it/s]
                   all         51         87      0.469      0.442      0.396      0.225

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    129/499      10.2G    0.03187    0.01716    0.01813         29        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.08it/s]
                   all         51         87      0.737      0.465      0.543       0.37

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    130/499      10.2G    0.03026    0.01564     0.0209         10        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.25it/s]
                   all         51         87      0.542      0.384      0.441       0.29

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    131/499      10.2G    0.03057    0.01587    0.02101         11        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.35it/s]
                   all         51         87      0.557      0.431      0.449      0.301

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    132/499      10.2G    0.03152    0.01635    0.02032         23        640: 100% 15/15 [00:08<00:00,  1.73it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.03s/it]
                   all         51         87      0.619      0.598      0.523      0.343

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    133/499      10.2G    0.03056    0.01554    0.02062         14        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.11it/s]
                   all         51         87      0.733      0.509      0.577      0.394

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    134/499      10.2G    0.03212    0.01611    0.02068         17        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.10it/s]
                   all         51         87      0.567      0.484      0.472      0.312

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    135/499      10.2G    0.03031    0.01521    0.01986         15        640: 100% 15/15 [00:09<00:00,  1.65it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.31it/s]
                   all         51         87      0.418       0.46      0.374      0.239

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    136/499      10.2G    0.03002    0.01572    0.01877         19        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.36it/s]
                   all         51         87       0.56      0.378      0.397      0.272

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    137/499      10.2G    0.02983    0.01558     0.0193         26        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.26it/s]
                   all         51         87       0.64      0.551      0.492      0.337

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    138/499      10.2G    0.03028    0.01533     0.0202         19        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.15it/s]
                   all         51         87      0.596        0.5      0.525      0.376

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    139/499      10.2G     0.0295    0.01589    0.01926         22        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.25it/s]
                   all         51         87      0.403      0.445      0.394      0.261

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    140/499      10.2G     0.0312    0.01677    0.01998         24        640: 100% 15/15 [00:08<00:00,  1.81it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.07it/s]
                   all         51         87      0.571      0.561      0.486       0.33

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    141/499      10.2G     0.0302    0.01581    0.01914         21        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.26it/s]
                   all         51         87      0.579      0.561      0.516      0.335

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    142/499      10.2G    0.03048    0.01612    0.01928         18        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.12it/s]
                   all         51         87      0.577      0.599      0.558      0.394

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    143/499      10.2G    0.02982    0.01471     0.0186         14        640: 100% 15/15 [00:09<00:00,  1.54it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.25s/it]
                   all         51         87      0.612      0.532      0.499      0.339

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    144/499      10.2G    0.03201    0.01665    0.02021         15        640: 100% 15/15 [00:09<00:00,  1.64it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.37it/s]
                   all         51         87      0.649      0.522      0.579      0.403

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    145/499      10.2G    0.03132    0.01452    0.02015         11        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.13it/s]
                   all         51         87      0.698      0.607      0.579      0.391

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    146/499      10.2G    0.02918    0.01473    0.01849         17        640: 100% 15/15 [00:08<00:00,  1.83it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.13it/s]
                   all         51         87      0.609      0.577       0.56      0.374

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    147/499      10.2G    0.03092    0.01579    0.02181         18        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.32it/s]
                   all         51         87      0.582      0.575      0.534      0.347

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    148/499      10.2G    0.03147    0.01441    0.01928          7        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.04it/s]
                   all         51         87      0.685      0.603       0.59      0.388

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    149/499      10.2G    0.03036    0.01542     0.0199         16        640: 100% 15/15 [00:08<00:00,  1.72it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:02<00:00,  2.57s/it]
                   all         51         87       0.71       0.47      0.491      0.309

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    150/499      10.2G    0.03064    0.01537    0.01938         20        640: 100% 15/15 [00:08<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.04it/s]
                   all         51         87      0.567      0.486      0.472      0.332

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    151/499      10.2G    0.02983    0.01577     0.0205         24        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.18it/s]
                   all         51         87      0.484      0.546      0.501      0.326

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    152/499      10.2G    0.03009    0.01614    0.02113         18        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.28it/s]
                   all         51         87      0.609      0.543      0.526      0.371

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    153/499      10.2G    0.03237    0.01612    0.01922         13        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.25it/s]
                   all         51         87      0.623      0.533      0.537      0.372

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    154/499      10.2G    0.03111    0.01563    0.01883         23        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.43it/s]
                   all         51         87      0.527      0.465      0.457      0.313

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    155/499      10.2G    0.02912    0.01477    0.01944         21        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.06it/s]
                   all         51         87      0.515      0.459      0.399      0.281

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    156/499      10.2G    0.02932    0.01527    0.01727         24        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.42it/s]
                   all         51         87      0.473      0.468      0.447      0.293

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    157/499      10.2G    0.03029    0.01493    0.01994         23        640: 100% 15/15 [00:08<00:00,  1.74it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.21it/s]
                   all         51         87      0.611      0.522      0.508      0.356

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    158/499      10.2G    0.03005    0.01518     0.0202         18        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.30it/s]
                   all         51         87       0.69        0.5      0.523      0.386

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    159/499      10.2G    0.02892     0.0152    0.01897         19        640: 100% 15/15 [00:08<00:00,  1.70it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.27it/s]
                   all         51         87      0.532      0.547      0.481      0.349

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    160/499      10.2G     0.0292    0.01514    0.01905         19        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.05s/it]
                   all         51         87      0.654      0.567       0.57      0.383

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    161/499      10.2G    0.02917    0.01554    0.01799         26        640: 100% 15/15 [00:10<00:00,  1.46it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.11it/s]
                   all         51         87      0.697      0.596      0.578      0.387

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    162/499      10.2G    0.03173    0.01525    0.02051         23        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.17it/s]
                   all         51         87      0.697      0.523       0.54       0.37

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    163/499      10.2G    0.03036    0.01566     0.0186         28        640: 100% 15/15 [00:08<00:00,  1.82it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.17it/s]
                   all         51         87      0.725      0.448      0.506      0.352

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    164/499      10.2G    0.02857    0.01485    0.02117         22        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.15it/s]
                   all         51         87       0.56      0.575      0.512       0.38

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    165/499      10.2G     0.0311    0.01544    0.01761         20        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.12it/s]
                   all         51         87      0.625      0.579       0.56      0.381

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    166/499      10.2G    0.03062    0.01453    0.01915         17        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.17it/s]
                   all         51         87      0.651      0.502      0.553      0.382

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    167/499      10.2G    0.02988    0.01572    0.02184         25        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.17it/s]
                   all         51         87      0.738      0.563      0.613      0.418

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    168/499      10.2G    0.02862    0.01533    0.02038         16        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.32it/s]
                   all         51         87       0.63      0.578      0.568      0.411

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    169/499      10.2G    0.02997    0.01591     0.0186         23        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.27it/s]
                   all         51         87      0.542      0.507      0.518      0.357

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    170/499      10.2G    0.02991    0.01616    0.01962         29        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.14it/s]
                   all         51         87      0.626      0.467      0.496      0.364

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    171/499      10.2G    0.02886    0.01527    0.01966         16        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.12it/s]
                   all         51         87      0.517      0.394      0.425      0.314

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    172/499      10.2G    0.02965     0.0147    0.02007         26        640: 100% 15/15 [00:08<00:00,  1.73it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.16it/s]
                   all         51         87      0.581      0.491      0.457      0.348

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    173/499      10.2G    0.02918    0.01485    0.01813         14        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.30it/s]
                   all         51         87      0.653      0.557      0.555      0.371

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    174/499      10.2G    0.03008    0.01421    0.01889         23        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.18it/s]
                   all         51         87      0.594      0.544      0.533      0.368

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    175/499      10.2G    0.03022    0.01455    0.01805         15        640: 100% 15/15 [00:08<00:00,  1.81it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.26it/s]
                   all         51         87      0.599       0.49      0.456      0.312

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    176/499      10.2G    0.02969    0.01424     0.0204         13        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.07it/s]
                   all         51         87      0.483      0.436      0.417      0.275

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    177/499      10.2G     0.0282    0.01447    0.01898         17        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.28it/s]
                   all         51         87      0.464      0.546      0.444      0.324

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    178/499      10.2G    0.02897    0.01491    0.01854         21        640: 100% 15/15 [00:10<00:00,  1.49it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.37s/it]
                   all         51         87      0.468      0.564       0.46      0.305

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    179/499      10.2G    0.02979    0.01504    0.01853         23        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.12it/s]
                   all         51         87      0.597       0.44      0.413      0.265

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    180/499      10.2G    0.02843    0.01495    0.02021         23        640: 100% 15/15 [00:08<00:00,  1.81it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.25it/s]
                   all         51         87      0.522      0.464       0.43      0.267

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    181/499      10.2G    0.03007    0.01477    0.01831         16        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.20it/s]
                   all         51         87      0.616      0.466      0.497      0.344

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    182/499      10.2G     0.0288    0.01531    0.02033         23        640: 100% 15/15 [00:08<00:00,  1.83it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.17it/s]
                   all         51         87      0.735       0.51      0.535      0.372

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    183/499      10.2G     0.0282    0.01488    0.01946         21        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.08it/s]
                   all         51         87      0.505       0.44      0.435      0.296

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    184/499      10.2G     0.0297    0.01498    0.02277         16        640: 100% 15/15 [00:08<00:00,  1.82it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.10it/s]
                   all         51         87      0.651      0.526      0.475      0.315

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    185/499      10.2G     0.0299    0.01442    0.01879         16        640: 100% 15/15 [00:08<00:00,  1.83it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.20it/s]
                   all         51         87      0.702      0.533      0.518       0.35

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    186/499      10.2G    0.02933    0.01398    0.01866         17        640: 100% 15/15 [00:08<00:00,  1.82it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.27it/s]
                   all         51         87      0.603      0.576      0.507      0.375

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    187/499      10.2G    0.02917     0.0145    0.02062         17        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.17it/s]
                   all         51         87      0.602      0.552      0.524      0.368

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    188/499      10.2G    0.02923    0.01422    0.01981         20        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.13it/s]
                   all         51         87       0.56      0.607      0.544      0.385

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    189/499      10.2G    0.03006    0.01465    0.01841         17        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.08it/s]
                   all         51         87       0.61      0.606      0.537      0.379

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    190/499      10.2G    0.02883    0.01491    0.01869         23        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.18it/s]
                   all         51         87      0.689      0.603      0.565      0.398

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    191/499      10.2G    0.02956    0.01553    0.02037         29        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.18it/s]
                   all         51         87      0.545      0.567      0.539      0.396

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    192/499      10.2G    0.03106    0.01518    0.02167         15        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.20it/s]
                   all         51         87      0.583      0.486      0.486      0.324

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    193/499      10.2G    0.02885    0.01395     0.0189         11        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.03it/s]
                   all         51         87      0.626      0.507      0.491      0.346

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    194/499      10.2G    0.02809    0.01461    0.01954         27        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.04it/s]
                   all         51         87      0.594       0.53      0.503      0.364

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    195/499      10.2G    0.03101    0.01418    0.01978         11        640: 100% 15/15 [00:08<00:00,  1.83it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.02s/it]
                   all         51         87      0.601      0.599      0.559      0.415

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    196/499      10.2G    0.02779    0.01464    0.02034         17        640: 100% 15/15 [00:10<00:00,  1.41it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.38it/s]
                   all         51         87      0.596      0.601      0.535      0.403

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    197/499      10.2G     0.0294    0.01455     0.0194         20        640: 100% 15/15 [00:09<00:00,  1.67it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.13it/s]
                   all         51         87       0.63      0.589      0.535      0.386

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    198/499      10.2G    0.02796    0.01478     0.0207         26        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.05it/s]
                   all         51         87       0.66      0.604      0.582      0.422

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    199/499      10.2G    0.02743    0.01454    0.01656         20        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:02<00:00,  2.56s/it]
                   all         51         87      0.703      0.584      0.553      0.382

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    200/499      10.2G    0.02888    0.01445    0.01998         19        640: 100% 15/15 [00:09<00:00,  1.61it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.12it/s]
                   all         51         87      0.693      0.531      0.552      0.376

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    201/499      10.2G    0.02806    0.01565    0.01885         21        640: 100% 15/15 [00:08<00:00,  1.81it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.06it/s]
                   all         51         87      0.664      0.529      0.534      0.375

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    202/499      10.2G    0.02938    0.01506    0.02131         31        640: 100% 15/15 [00:08<00:00,  1.82it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.20it/s]
                   all         51         87      0.538      0.496      0.469      0.336

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    203/499      10.2G    0.02835     0.0144    0.01929         14        640: 100% 15/15 [00:08<00:00,  1.72it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.13it/s]
                   all         51         87      0.652      0.495       0.49      0.344

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    204/499      10.2G    0.02838    0.01517     0.0173         20        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.33it/s]
                   all         51         87      0.682      0.509      0.546      0.402

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    205/499      10.2G    0.02686    0.01392    0.01791         17        640: 100% 15/15 [00:08<00:00,  1.82it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.18it/s]
                   all         51         87      0.705      0.584      0.571      0.418

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    206/499      10.2G    0.02807    0.01539    0.01891         32        640: 100% 15/15 [00:08<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.24it/s]
                   all         51         87      0.504       0.48      0.404      0.278

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    207/499      10.2G    0.02789    0.01438    0.02028         17        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.02it/s]
                   all         51         87      0.636      0.553      0.526       0.36

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    208/499      10.2G     0.0288     0.0142    0.01876         18        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.14it/s]
                   all         51         87      0.598       0.53      0.486      0.344

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    209/499      10.2G     0.0281    0.01361    0.01914         14        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.14it/s]
                   all         51         87      0.561       0.56      0.503      0.383

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    210/499      10.2G    0.02812    0.01393     0.0181         21        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.19it/s]
                   all         51         87      0.615      0.592      0.568      0.423

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    211/499      10.2G    0.02843    0.01482    0.01933         15        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.11it/s]
                   all         51         87      0.661      0.595      0.565      0.423

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    212/499      10.2G      0.028    0.01372    0.01792          9        640: 100% 15/15 [00:08<00:00,  1.72it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.40it/s]
                   all         51         87      0.726      0.536      0.559      0.422

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    213/499      10.2G    0.02769    0.01465    0.01792         32        640: 100% 15/15 [00:11<00:00,  1.35it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.35it/s]
                   all         51         87      0.669      0.535       0.54      0.398

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    214/499      10.2G     0.0279    0.01443    0.02282         24        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.24it/s]
                   all         51         87      0.683      0.556      0.539      0.357

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    215/499      10.2G    0.02787     0.0139     0.0191         15        640: 100% 15/15 [00:08<00:00,  1.72it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.30it/s]
                   all         51         87      0.619      0.556      0.541      0.406

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    216/499      10.2G    0.02747    0.01444    0.01821         20        640: 100% 15/15 [00:08<00:00,  1.73it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.05it/s]
                   all         51         87      0.691      0.434      0.483      0.351

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    217/499      10.2G    0.02843    0.01423    0.01804         12        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.17it/s]
                   all         51         87      0.652       0.54      0.506      0.368

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    218/499      10.2G    0.02784    0.01382    0.01795         16        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.13it/s]
                   all         51         87      0.571      0.548      0.528      0.368

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    219/499      10.2G    0.02875     0.0136    0.01688         16        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.34it/s]
                   all         51         87      0.552      0.524       0.45      0.307

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    220/499      10.2G    0.02591    0.01346    0.02011         16        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.32it/s]
                   all         51         87      0.608      0.514      0.514      0.369

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    221/499      10.2G    0.02859    0.01491    0.01926         23        640: 100% 15/15 [00:08<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.31it/s]
                   all         51         87      0.646      0.528      0.532      0.397

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    222/499      10.2G    0.02684    0.01415    0.01813         24        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.42it/s]
                   all         51         87      0.549      0.515      0.487      0.365

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    223/499      10.2G    0.02765    0.01391     0.0199          9        640: 100% 15/15 [00:08<00:00,  1.73it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.31it/s]
                   all         51         87       0.65      0.499       0.54      0.397

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    224/499      10.2G    0.02902    0.01471    0.01702         21        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.16it/s]
                   all         51         87      0.586      0.492      0.499      0.377

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    225/499      10.2G    0.02615    0.01387    0.01914         21        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.11it/s]
                   all         51         87      0.645      0.451      0.489      0.379

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    226/499      10.2G    0.02825    0.01366    0.01854          9        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.09it/s]
                   all         51         87      0.572      0.438      0.414      0.311

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    227/499      10.2G    0.02955    0.01381    0.01907         19        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.22it/s]
                   all         51         87      0.634      0.495      0.491      0.355

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    228/499      10.2G    0.02818    0.01429    0.01809         21        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.19it/s]
                   all         51         87      0.649      0.562      0.534      0.374

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    229/499      10.2G    0.02917    0.01451    0.01896         27        640: 100% 15/15 [00:08<00:00,  1.70it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.37it/s]
                   all         51         87      0.619       0.51      0.503      0.369

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    230/499      10.2G    0.02783    0.01368    0.01956         20        640: 100% 15/15 [00:10<00:00,  1.41it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.01it/s]
                   all         51         87      0.603      0.585      0.549      0.398

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    231/499      10.2G    0.02621    0.01376    0.01862         17        640: 100% 15/15 [00:08<00:00,  1.71it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.22it/s]
                   all         51         87      0.771      0.493       0.54      0.394

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    232/499      10.2G    0.02767    0.01364    0.01928         24        640: 100% 15/15 [00:08<00:00,  1.74it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.31it/s]
                   all         51         87      0.737      0.504      0.603      0.441

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    233/499      10.2G    0.02624    0.01478    0.01882         30        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.21it/s]
                   all         51         87      0.757      0.489      0.578      0.416

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    234/499      10.2G    0.02696    0.01416    0.01871         14        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.10it/s]
                   all         51         87      0.584      0.564      0.537      0.367

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    235/499      10.2G    0.02797    0.01414     0.0161         31        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.08it/s]
                   all         51         87      0.726      0.489      0.561      0.404

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    236/499      10.2G      0.029     0.0146    0.01756         17        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.15it/s]
                   all         51         87      0.567      0.534       0.51      0.353

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    237/499      10.2G    0.03011    0.01395    0.01806         21        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.28it/s]
                   all         51         87      0.625       0.54      0.533      0.371

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    238/499      10.2G    0.02773    0.01385    0.01682         39        640: 100% 15/15 [00:08<00:00,  1.72it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.05it/s]
                   all         51         87      0.712      0.481      0.518       0.37

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    239/499      10.2G    0.02886     0.0148    0.01864         26        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.12it/s]
                   all         51         87      0.642      0.516      0.541      0.398

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    240/499      10.2G    0.02563    0.01321    0.02052         10        640: 100% 15/15 [00:08<00:00,  1.81it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.24it/s]
                   all         51         87      0.705       0.54      0.553      0.378

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    241/499      10.2G    0.02719    0.01331    0.01744         23        640: 100% 15/15 [00:08<00:00,  1.81it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.13it/s]
                   all         51         87      0.748      0.486      0.593      0.423

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    242/499      10.2G    0.02768    0.01369    0.01777         16        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.11it/s]
                   all         51         87      0.624      0.548      0.565      0.399

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    243/499      10.2G    0.02697    0.01401    0.01711         22        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.09it/s]
                   all         51         87      0.619      0.517      0.531       0.36

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    244/499      10.2G    0.02628    0.01381    0.01864         16        640: 100% 15/15 [00:08<00:00,  1.83it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.15it/s]
                   all         51         87      0.715      0.442      0.543      0.352

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    245/499      10.2G    0.02726    0.01355    0.01989         18        640: 100% 15/15 [00:08<00:00,  1.74it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.06it/s]
                   all         51         87      0.557      0.515      0.457      0.306

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    246/499      10.2G    0.02614    0.01378    0.01816         18        640: 100% 15/15 [00:08<00:00,  1.82it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.17it/s]
                   all         51         87      0.548      0.528      0.423      0.299

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    247/499      10.2G    0.02864     0.0133    0.02245          8        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.05it/s]
                   all         51         87      0.488      0.515      0.431      0.314

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    248/499      10.2G    0.02645     0.0125    0.01737         18        640: 100% 15/15 [00:10<00:00,  1.47it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.12it/s]
                   all         51         87      0.641      0.533      0.524      0.389

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    249/499      10.2G    0.02817    0.01304    0.01916         13        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:02<00:00,  2.48s/it]
                   all         51         87      0.482      0.475      0.472       0.35

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    250/499      10.2G    0.02835    0.01408    0.01894         14        640: 100% 15/15 [00:08<00:00,  1.70it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.01s/it]
                   all         51         87      0.673      0.405      0.483      0.364

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    251/499      10.2G    0.02836    0.01377    0.01855         18        640: 100% 15/15 [00:08<00:00,  1.73it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.34it/s]
                   all         51         87      0.735      0.498      0.555      0.415

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    252/499      10.2G    0.02732    0.01406     0.0164         16        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.33it/s]
                   all         51         87      0.548      0.541      0.509      0.373

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    253/499      10.2G    0.02743    0.01381    0.01585         21        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.09it/s]
                   all         51         87      0.574      0.505      0.491      0.351

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    254/499      10.2G     0.0261    0.01314    0.01972         12        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.20it/s]
                   all         51         87      0.431      0.463      0.389      0.256

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    255/499      10.2G     0.0279    0.01411    0.01845         16        640: 100% 15/15 [00:08<00:00,  1.69it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.31it/s]
                   all         51         87      0.626      0.518      0.515      0.371

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    256/499      10.2G    0.02672    0.01365    0.02073         13        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.27it/s]
                   all         51         87      0.598      0.467      0.462      0.324

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    257/499      10.2G    0.02731    0.01432    0.01825         30        640: 100% 15/15 [00:08<00:00,  1.73it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.30it/s]
                   all         51         87      0.724      0.486      0.547      0.396

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    258/499      10.2G    0.02885    0.01382    0.01592         22        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.09it/s]
                   all         51         87      0.645      0.505      0.531      0.386

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    259/499      10.2G    0.02551    0.01321    0.01687         12        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.29it/s]
                   all         51         87      0.546      0.556      0.475      0.343

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    260/499      10.2G    0.02638    0.01365    0.01922         13        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.17it/s]
                   all         51         87       0.71      0.551      0.547      0.393

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    261/499      10.2G    0.02615    0.01318    0.01884         18        640: 100% 15/15 [00:08<00:00,  1.71it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.29it/s]
                   all         51         87      0.677      0.568      0.524      0.379

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    262/499      10.2G    0.02607     0.0145    0.01751         29        640: 100% 15/15 [00:08<00:00,  1.82it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.12it/s]
                   all         51         87      0.695      0.577      0.552      0.396

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    263/499      10.2G    0.02656    0.01413    0.01848         20        640: 100% 15/15 [00:08<00:00,  1.82it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.20it/s]
                   all         51         87      0.621      0.532       0.52      0.352

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    264/499      10.2G    0.02718    0.01305    0.01741         17        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.05s/it]
                   all         51         87      0.571      0.533      0.522      0.367

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    265/499      10.2G    0.02601    0.01282     0.0171         12        640: 100% 15/15 [00:10<00:00,  1.41it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.18it/s]
                   all         51         87       0.56      0.576      0.547      0.385

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    266/499      10.2G    0.02733     0.0138     0.0171         18        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.27it/s]
                   all         51         87      0.671      0.523       0.53      0.374

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    267/499      10.2G    0.02662    0.01246    0.01828         13        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.23it/s]
                   all         51         87        0.7       0.52      0.551      0.392

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    268/499      10.2G    0.02593    0.01275    0.01669         19        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.22it/s]
                   all         51         87      0.727      0.542      0.577       0.41

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    269/499      10.2G    0.02666    0.01322    0.01731         17        640: 100% 15/15 [00:08<00:00,  1.74it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.33it/s]
                   all         51         87      0.558      0.587      0.527      0.383

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    270/499      10.2G    0.02737    0.01335    0.01758         15        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.36it/s]
                   all         51         87      0.525      0.531      0.454       0.33

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    271/499      10.2G     0.0257    0.01361    0.01755         26        640: 100% 15/15 [00:08<00:00,  1.73it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.10it/s]
                   all         51         87      0.663       0.51      0.509      0.373

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    272/499      10.2G    0.02577    0.01369    0.01832          8        640: 100% 15/15 [00:08<00:00,  1.82it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.33it/s]
                   all         51         87      0.687      0.474        0.5      0.355

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    273/499      10.2G    0.02727    0.01433     0.0177         33        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.25it/s]
                   all         51         87      0.597      0.505      0.483      0.351

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    274/499      10.2G    0.02643    0.01366    0.01794         13        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.03it/s]
                   all         51         87      0.535      0.501      0.438        0.3

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    275/499      10.2G    0.02635    0.01337    0.01896         26        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.33it/s]
                   all         51         87       0.59      0.484      0.476      0.327

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    276/499      10.2G    0.02518    0.01319    0.01684         23        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.13it/s]
                   all         51         87      0.539      0.571      0.492      0.331

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    277/499      10.2G     0.0275    0.01346    0.01765         31        640: 100% 15/15 [00:08<00:00,  1.81it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.12it/s]
                   all         51         87      0.627      0.526      0.485      0.329

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    278/499      10.2G    0.02521    0.01318    0.01868         11        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.31it/s]
                   all         51         87      0.667      0.531      0.549        0.4

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    279/499      10.2G    0.02765    0.01379    0.01671         26        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.26it/s]
                   all         51         87      0.646      0.537      0.536      0.373

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    280/499      10.2G    0.02576    0.01337    0.01826         11        640: 100% 15/15 [00:08<00:00,  1.69it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.11it/s]
                   all         51         87       0.57      0.529      0.496      0.348

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    281/499      10.2G    0.02712    0.01328    0.02267         17        640: 100% 15/15 [00:08<00:00,  1.72it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.52it/s]
                   all         51         87      0.694       0.45      0.498      0.333

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    282/499      10.2G    0.02649    0.01352    0.01794         34        640: 100% 15/15 [00:10<00:00,  1.43it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.22it/s]
                   all         51         87      0.709      0.502      0.522      0.352

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    283/499      10.2G    0.02647    0.01365    0.02023         22        640: 100% 15/15 [00:08<00:00,  1.69it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.29it/s]
                   all         51         87      0.675      0.525      0.522      0.348

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    284/499      10.2G    0.02482    0.01275    0.01729         14        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.17it/s]
                   all         51         87      0.624      0.497      0.499      0.341

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    285/499      10.2G    0.02608    0.01307    0.01784         22        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.25it/s]
                   all         51         87      0.651      0.553      0.534      0.374

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    286/499      10.2G    0.02616    0.01318    0.01691         20        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.11it/s]
                   all         51         87       0.69      0.493      0.511      0.362

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    287/499      10.2G    0.02511    0.01271    0.01899         17        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.32it/s]
                   all         51         87      0.627      0.511      0.529      0.385

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    288/499      10.2G    0.02696    0.01409     0.0174         19        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.23it/s]
                   all         51         87      0.594      0.568      0.509      0.376

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    289/499      10.2G    0.02532    0.01366     0.0168         28        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.19it/s]
                   all         51         87      0.542      0.474      0.452      0.325

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    290/499      10.2G    0.02525     0.0147    0.01731         24        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.36it/s]
                   all         51         87      0.639      0.514      0.491      0.358

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    291/499      10.2G    0.02693    0.01295    0.01684         14        640: 100% 15/15 [00:08<00:00,  1.74it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.32it/s]
                   all         51         87      0.641      0.516      0.511      0.364

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    292/499      10.2G    0.02499    0.01344     0.0181         21        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.18it/s]
                   all         51         87      0.593      0.545      0.513      0.375

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    293/499      10.2G    0.02655    0.01335    0.01852         16        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.14it/s]
                   all         51         87      0.546      0.539      0.497      0.356

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    294/499      10.2G    0.02646    0.01338    0.01664         18        640: 100% 15/15 [00:08<00:00,  1.74it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.09it/s]
                   all         51         87       0.64       0.52      0.563      0.375

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    295/499      10.2G    0.02639    0.01324    0.01658         14        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.17it/s]
                   all         51         87      0.604      0.497      0.497       0.34

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    296/499      10.2G    0.02604    0.01268    0.01825         18        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.11it/s]
                   all         51         87      0.484      0.541      0.473      0.324

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    297/499      10.2G     0.0259    0.01252    0.01891         20        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.33it/s]
                   all         51         87      0.716      0.501      0.537      0.384

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    298/499      10.2G    0.02608    0.01385    0.01664         27        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.11it/s]
                   all         51         87      0.688      0.488      0.516      0.373

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    299/499      10.2G    0.02605    0.01258     0.0173         21        640: 100% 15/15 [00:09<00:00,  1.58it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:04<00:00,  4.08s/it]
                   all         51         87      0.508      0.536      0.492      0.344

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    300/499      10.2G    0.02489    0.01308    0.01709         15        640: 100% 15/15 [00:08<00:00,  1.68it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.10it/s]
                   all         51         87      0.559      0.497      0.473      0.336

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    301/499      10.2G    0.02445     0.0132    0.01588         19        640: 100% 15/15 [00:08<00:00,  1.74it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.18it/s]
                   all         51         87      0.542      0.553      0.479      0.341

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    302/499      10.2G      0.026    0.01221    0.01652         18        640: 100% 15/15 [00:08<00:00,  1.82it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.26it/s]
                   all         51         87      0.586      0.522       0.48      0.344

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    303/499      10.2G    0.02586    0.01262    0.01824         15        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.16it/s]
                   all         51         87      0.588      0.496       0.47      0.335

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    304/499      10.2G    0.02544    0.01265    0.01837         15        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.12it/s]
                   all         51         87      0.664      0.495      0.523      0.381

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    305/499      10.2G    0.02537    0.01308    0.01791         20        640: 100% 15/15 [00:08<00:00,  1.83it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.17it/s]
                   all         51         87      0.706      0.473      0.512      0.366

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    306/499      10.2G    0.02565    0.01269    0.01585         23        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.30it/s]
                   all         51         87      0.602      0.557      0.505      0.358

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    307/499      10.2G     0.0262     0.0126    0.01778         13        640: 100% 15/15 [00:08<00:00,  1.69it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.27it/s]
                   all         51         87      0.714      0.525      0.492      0.334

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    308/499      10.2G    0.02442    0.01315    0.01696         23        640: 100% 15/15 [00:08<00:00,  1.83it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.16it/s]
                   all         51         87      0.692      0.543       0.54      0.368

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    309/499      10.2G    0.02534    0.01302    0.01706         21        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.10it/s]
                   all         51         87      0.593      0.527        0.5      0.356

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    310/499      10.2G    0.02628    0.01321    0.01937         16        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.38it/s]
                   all         51         87      0.611      0.522      0.485      0.351

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    311/499      10.2G    0.02507    0.01267    0.01639         22        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.07it/s]
                   all         51         87      0.542      0.528      0.488      0.344

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    312/499      10.2G    0.02489    0.01227    0.01701         12        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.13it/s]
                   all         51         87      0.619      0.483      0.473      0.337

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    313/499      10.2G     0.0273    0.01198    0.01748         13        640: 100% 15/15 [00:08<00:00,  1.74it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.06it/s]
                   all         51         87      0.706      0.456      0.447      0.322

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    314/499      10.2G    0.02557    0.01181    0.01831         17        640: 100% 15/15 [00:08<00:00,  1.83it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.06it/s]
                   all         51         87      0.634      0.553      0.514      0.365

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    315/499      10.2G    0.02498    0.01235    0.01738         13        640: 100% 15/15 [00:08<00:00,  1.83it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.06it/s]
                   all         51         87      0.595      0.536      0.498      0.344

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    316/499      10.2G    0.02488    0.01294    0.01822         11        640: 100% 15/15 [00:09<00:00,  1.52it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:01<00:00,  1.04s/it]
                   all         51         87      0.549      0.553      0.505      0.356

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    317/499      10.2G      0.026    0.01317    0.02012         25        640: 100% 15/15 [00:08<00:00,  1.69it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.28it/s]
                   all         51         87      0.685      0.481      0.509      0.366

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    318/499      10.2G    0.02547    0.01258    0.01811         18        640: 100% 15/15 [00:08<00:00,  1.82it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.20it/s]
                   all         51         87       0.67      0.487      0.501      0.364

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    319/499      10.2G    0.02489    0.01193    0.01775         17        640: 100% 15/15 [00:08<00:00,  1.78it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.25it/s]
                   all         51         87      0.532      0.581      0.544        0.4

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    320/499      10.2G    0.02476    0.01335    0.01566         26        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.08it/s]
                   all         51         87      0.586      0.517      0.515      0.379

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    321/499      10.2G     0.0252    0.01328      0.018         17        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.15it/s]
                   all         51         87      0.684      0.479       0.52      0.387

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    322/499      10.2G    0.02526    0.01284     0.0182         20        640: 100% 15/15 [00:08<00:00,  1.75it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.24it/s]
                   all         51         87      0.707      0.503      0.535      0.399

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    323/499      10.2G    0.02444    0.01341    0.01604         21        640: 100% 15/15 [00:08<00:00,  1.74it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.12it/s]
                   all         51         87      0.662      0.515      0.513      0.385

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    324/499      10.2G    0.02441    0.01238    0.01934         19        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.20it/s]
                   all         51         87      0.534      0.574      0.502      0.379

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    325/499      10.2G    0.02525    0.01284    0.01865         17        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.37it/s]
                   all         51         87      0.505      0.515      0.466      0.348

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    326/499      10.2G    0.02458    0.01244     0.0175         17        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.40it/s]
                   all         51         87      0.633      0.489      0.468      0.359

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    327/499      10.2G    0.02383     0.0127     0.0178         14        640: 100% 15/15 [00:08<00:00,  1.76it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.31it/s]
                   all         51         87      0.738      0.519      0.525      0.395

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    328/499      10.2G    0.02451    0.01282    0.01846         35        640: 100% 15/15 [00:08<00:00,  1.77it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.28it/s]
                   all         51         87      0.738      0.545      0.548      0.399

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    329/499      10.2G    0.02614    0.01244    0.01884         12        640: 100% 15/15 [00:08<00:00,  1.72it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.10it/s]
                   all         51         87      0.745      0.495      0.529      0.384

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    330/499      10.2G    0.02439    0.01283    0.01608         13        640: 100% 15/15 [00:08<00:00,  1.79it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.28it/s]
                   all         51         87       0.65      0.513      0.499       0.36

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    331/499      10.2G    0.02574    0.01302    0.01575         17        640: 100% 15/15 [00:08<00:00,  1.71it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.22it/s]
                   all         51         87      0.757      0.491      0.547      0.408

      Epoch    GPU_mem   box_loss   obj_loss   cls_loss  Instances       Size
    332/499      10.2G    0.02517    0.01198    0.01783         20        640: 100% 15/15 [00:08<00:00,  1.80it/s]
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.28it/s]
                   all         51         87      0.782      0.525      0.549      0.419
Stopping training early as no improvement observed in last 100 epochs. Best results observed at epoch 232, best model saved as best.pt.
To update EarlyStopping(patience=100) pass a new patience value, i.e. `python train.py --patience 300` or use `--patience 0` to disable EarlyStopping.

333 epochs completed in 0.949 hours.
Optimizer stripped from runs/train/exp/weights/last.pt, 14.5MB
Optimizer stripped from runs/train/exp/weights/best.pt, 14.5MB

Validating runs/train/exp/weights/best.pt...
Fusing layers... 
Model summary: 157 layers, 7018216 parameters, 0 gradients, 15.8 GFLOPs
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 1/1 [00:00<00:00,  1.70it/s]
                   all         51         87      0.737      0.504      0.603       0.44
         NEEDLE HOLDER         51         41      0.792       0.28      0.466       0.33
             RETRACTOR         51         17      0.765      0.647      0.716      0.511
               SCALPEL         51         29      0.653      0.586      0.626      0.479
     ```
</details>

### Evidências do treinamento

![Gráficos de Perdas](https://user-images.githubusercontent.com/115883399/200435577-e44592fc-1cfb-4444-ba4a-94457154e4cf.png)
![Matriz de Confusão](https://user-images.githubusercontent.com/115883399/200435805-8d7c33e7-0e80-49c2-b0ce-ac853d01737a.png)


## Roboflow

[/especializacao/supermarket](https://universe.roboflow.com/especializao/surgeryinstruments)

## HuggingFace

[HuggingFace](https://huggingface.co/spaces/camilacorreamelo/medicalDetection)
