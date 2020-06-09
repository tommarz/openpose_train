import os
from generateLmdbFile import generateLmdbFile, generateNegativesLmdbFile

sCaffePythonPath = os.path.join('../../openpose_caffe_train', 'python/')
sDatasetFolderLmdb = '../dataset/'
# sDatasetFolderLmdb = '/mnt/DataUbuntu/openpose_train/dataset/'
sDatasetFolder = '../dataset/'
# COCO
sCocoDatasetFolder = sDatasetFolderLmdb + 'COCO/'
sCocoLmdbPath = sDatasetFolderLmdb + 'lmdb_coco/'
sCocoImagesFolder = sCocoDatasetFolder + 'cocoapi/images/'
sCocoJsonFile = sCocoDatasetFolder + 'json/custom.json'
# FootCoco2017
sFootCoco2017DatasetFolder = sCocoDatasetFolder
sFootCoco2017LmdbPath = sDatasetFolderLmdb + 'lmdb_coco2017_foot/'
sFootCoco2017ImagesFolder = sCocoImagesFolder
sFootCoco2017JsonFile = sCocoDatasetFolder + 'json/coco2017_foot.json'
# MPII
sMpiiDatasetFolder = sDatasetFolder + 'MPII/'
sMpiiLmdbPath = sDatasetFolderLmdb + 'lmdb_mpii/'
sMpiiImagesFolder = sMpiiDatasetFolder + 'images/'
sMpiiMaskFolder = sMpiiDatasetFolder + 'mask/'
sMpiiJsonFile = sMpiiDatasetFolder + 'json/root_mpii.json'
# Face - frgc
# sFaceFrgcDatasetFolder = sDatasetFolder + 'face/'
sFaceFrgcDatasetFolder = '/media/posefs3b/Users/gines/Datasets/face/tomas_ready/'
sFaceFrgcLmdbPath = sDatasetFolderLmdb + 'lmdb_face_frgc/'
sFaceFrgcImagesFolder = sFaceFrgcDatasetFolder + 'frgc_train/'
sFaceFrgcJsonFile = sCocoDatasetFolder + 'json/face70_frgc.json'
# Face - multipie
# sFaceMultipieDatasetFolder = sDatasetFolder + 'face/'
sFaceMultipieDatasetFolder = '/media/posefs3b/Users/gines/Datasets/face/tomas_ready/'
sFaceMultipieLmdbPath = sDatasetFolderLmdb + 'lmdb_face_multipie/'
sFaceMultipieImagesFolder = sFaceMultipieDatasetFolder + 'multipie_train/'
sFaceMultipieJsonFile = sCocoDatasetFolder + 'json/face70_multipie.json'
# Face - face_mask_out
# sFaceMaskOutDatasetFolder = sDatasetFolder + 'face/'
sFaceMaskOutDatasetFolder = '/media/posefs3b/Users/gines/Datasets/face/tomas_ready/'
sFaceMaskOutLmdbPath = sDatasetFolderLmdb + 'lmdb_face_mask_out/'
sFaceMaskOutImagesFolder = sFaceMaskOutDatasetFolder + 'face_mask_out_train/'
sFaceMaskOutMaskFolder = sCocoImagesFolder + 'mask2017/face_mask_out_train/'
sFaceMaskOutJsonFile = sCocoDatasetFolder + 'json/face70_mask_out.json'
# Hand - Dome
sHandDomeDatasetFolder = sDatasetFolder + 'hand/'
sHandDomeLmdbPath = sDatasetFolderLmdb + 'lmdb_hand_dome/'
sHandDomeImagesFolder = sHandDomeDatasetFolder + 'hand143_panopticdb/imgs/'
sHandDomeJsonFile = sCocoDatasetFolder + 'json/hand21_dome.json'
sHandDomeMaskFolder = sCocoImagesFolder
# Hand - MPII
sHandMpiiDatasetFolder = sDatasetFolder + 'hand/'
sHandMpiiLmdbPath = sDatasetFolderLmdb + 'lmdb_hand_mpii/'
sHandMpiiImagesFolder = sHandMpiiDatasetFolder + 'hand_labels_v2/manual_train_v2/'
sHandMpiiJsonFile = sCocoDatasetFolder + 'json/hand42_mpii.json'
sHandMpiiMaskFolder = sCocoImagesFolder
# Dome
sDomeLmdbPath = sDatasetFolderLmdb + 'lmdb_dome135/'
sDomeImagesFolder = '/media/posefs0c/panopticdb/a4/hdImgs/'
sDomeJsonFile = sCocoDatasetFolder + 'json/dome135.json'

# MPII hand
sMpiiHandLmdbPath = sDatasetFolderLmdb + 'lmdb_mpii_hand/'
sMpiiHandImagesFolder = sDatasetFolder + 'COCO/Tomas/hand_labels/' + 'manual_train/'
sMpiiHandJsonFile = sDatasetFolder + 'dome/MPII_hand.json'
# # DomeDB
# #     # Option a: body
# # sDomeLmdbPath = sDatasetFolderLmdb + 'lmdb_dome/'
# # sDomeImagesFolder = '/media/posefs0c/panopticdb/a4/'
# # sDomeJsonFile = sDatasetFolder + 'dome/dome.json'
#     # Option b: body + hands
# sDomeLmdbPath = sDatasetFolderLmdb + 'lmdb_dome_bodyHand/'
# sDomeImagesFolder = '/media/posefs0c/panopticdb/a4/'
# sDomeJsonFile = sDatasetFolder + 'dome/dome_bodyHands.json'
# FootCoco2014
sFootCoco2014DatasetFolder = sCocoDatasetFolder
sFootCoco2014ImagesFolder = sCocoImagesFolder
sFootCoco2014LmdbPath = sDatasetFolderLmdb + 'lmdb_foot_coco2014/'
sFootCoco2014JsonFile = sCocoDatasetFolder + 'json/foot_coco2014.json'
# FootDome
sFootDomeLmdbPath = sDatasetFolderLmdb + 'lmdb_foot_dome_it1/'
sFootDomeImagesFolder = '/media/posefs0c/panopticdb/body_foot'
sFootDomeJsonFile = sDatasetFolder + 'dome/dome_foot_it1.json'

# Aayush labels - hands_wrist_LR
sHandWristLRLmdbPath = sDatasetFolderLmdb + 'lmdb_hands_wrist_LR/'
sHandWristLRImagesFolder = sDatasetFolder + 'COCO/hands_wrist_LR/'
sHandWristLRJsonFile = sDatasetFolder + 'COCO/json/hands_wrist_LR.json'
# Aayush labels - hand143_panopticdb
sHand143PanopticDbLmdbPath = sDatasetFolderLmdb + 'lmdb_hand143_panopticdb/'
sHand143PanopticDbImagesFolder = sDatasetFolder + 'COCO/hand143_panopticdb/'
sHand143PanopticDbJsonFile = sDatasetFolder + 'COCO/json/hand143_panopticdb.json'

# Car14
sCar14DatasetFolder = sDatasetFolder + 'COCO/'
sCar14LmdbPath = sDatasetFolderLmdb + 'lmdb_car_v1/'
sCar14ImagesFolder = sCar14DatasetFolder + 'car_dataset/Dataset/'
sCar14JsonFile = sCar14DatasetFolder + 'json/car_v1.json'

# Car22 - car-fusion
sCar22CFDatasetFolder = sDatasetFolder + 'COCO/'
sCar22CFLmdbPath = sDatasetFolderLmdb + 'lmdb_car22_carfusion/'
sCar22CFImagesFolder = '/media/posefs4b/User/hidrees/VehiclePoseEstimation/car-fusion/'
sCar22CFJsonFile = sCar22CFDatasetFolder + 'json/car22_carfusion.json'
sCar22CFMaskFolder = '/mnt/DataUbuntu/openpose_train/dataset/COCO/cocoapi/images/mask2017/car-fusion/'

# Car22 - pascal3d+
sCar22P3DatasetFolder = sDatasetFolder + 'COCO/'
sCar22P3LmdbPath = sDatasetFolderLmdb + 'lmdb_car22_pascal3dplus/'
sCar22P3ImagesFolder = '/media/posefs4b/User/hidrees/VehiclePoseEstimation/pascal3d+/'
sCar22P3JsonFile = sCar22P3DatasetFolder + 'json/car22_pascal3dplus.json'
sCar22P3MaskFolder = '/mnt/DataUbuntu/openpose_train/dataset/COCO/cocoapi/images/mask2017/pascal3d+/'

# Car22 - veri-776
sCar22V7DatasetFolder = sDatasetFolder + 'COCO/'
sCar22V7LmdbPath = sDatasetFolderLmdb + 'lmdb_car22_veri776/'
sCar22V7ImagesFolder = '/media/posefs4b/User/hidrees/VehiclePoseEstimation/veri-776/'
sCar22V7JsonFile = sCar22V7DatasetFolder + 'json/car22_veri776.json'
sCar22V7MaskFolder = '/mnt/DataUbuntu/openpose_train/dataset/COCO/cocoapi/images/mask2017/veri-776/'



# Negatives
# COCO background
sBackgroundLmdbPath = sDatasetFolderLmdb + 'lmdb_background/'
sBackgroundImagesFolder = sCocoImagesFolder + 'custom/'
sBackgroundJsonFile = sCocoDatasetFolder + 'json/coco_negatives.json'
# COCO car background
sCarBackgroundLmdbPath = sDatasetFolderLmdb + 'lmdb_car_background/'
sCarBackgroundImagesFolder = sCocoImagesFolder + 'custom/'
sCarBackgroundJsonFile = sCocoDatasetFolder + 'json/coco_negatives_cars.json'



if __name__ == "__main__":
    # Positives
    # Body and/or foot
    generateLmdbFile(sCocoLmdbPath, sCocoImagesFolder, sCocoJsonFile, sCaffePythonPath)
    # generateLmdbFile(sFootCoco2017LmdbPath, sFootCoco2017ImagesFolder, sFootCoco2017JsonFile, sCaffePythonPath)
    # generateLmdbFile(sMpiiLmdbPath, sMpiiImagesFolder, sMpiiJsonFile, sCaffePythonPath, sMpiiMaskFolder)
    # Face
    # generateLmdbFile(sFaceFrgcLmdbPath, sFaceFrgcImagesFolder, sFaceFrgcJsonFile, sCaffePythonPath)
    # generateLmdbFile(sFaceMultipieLmdbPath, sFaceMultipieImagesFolder, sFaceMultipieJsonFile, sCaffePythonPath)
    # generateLmdbFile(sFaceMaskOutLmdbPath, sFaceMaskOutImagesFolder, sFaceMaskOutJsonFile, sCaffePythonPath, sFaceMaskOutMaskFolder)
    # Hand
    # generateLmdbFile(sHandMpiiLmdbPath, sHandMpiiImagesFolder, sHandMpiiJsonFile, sCaffePythonPath, sHandMpiiMaskFolder)
    # generateLmdbFile(sHandDomeLmdbPath, sHandDomeImagesFolder, sHandDomeJsonFile, sCaffePythonPath, sHandDomeMaskFolder)
    # Dome
    # generateLmdbFile(sDomeLmdbPath, sDomeImagesFolder, sDomeJsonFile, sCaffePythonPath)

    # Others
    # generateLmdbFile(sDomeLmdbPath, sDomeImagesFolder, sDomeJsonFile, sCaffePythonPath)
    # generateLmdbFile(sMpiiHandLmdbPath, sMpiiHandImagesFolder, sMpiiHandJsonFile, sCaffePythonPath)
    # generateLmdbFile(sFootCoco2014LmdbPath, sFootCoco2014ImagesFolder, sFootCoco2014JsonFile, sCaffePythonPath)
    # generateLmdbFile(sFootDomeLmdbPath, sFootDomeImagesFolder, sFootDomeJsonFile, sCaffePythonPath)
    # generateLmdbFile(sHandWristLRLmdbPath, sHandWristLRImagesFolder, sHandWristLRJsonFile, sCaffePythonPath)
    # generateLmdbFile(sHand143PanopticDbLmdbPath, sHand143PanopticDbImagesFolder, sHand143PanopticDbJsonFile, sCaffePythonPath)
    # generateLmdbFile(sCar14LmdbPath, sCar14ImagesFolder, sCar14JsonFile, sCaffePythonPath)
    # generateLmdbFile(sCar22CFLmdbPath, sCar22CFImagesFolder, sCar22CFJsonFile, sCaffePythonPath, sCar22CFMaskFolder)
    # generateLmdbFile(sCar22P3LmdbPath, sCar22P3ImagesFolder, sCar22P3JsonFile, sCaffePythonPath, sCar22P3MaskFolder)
    # generateLmdbFile(sCar22V7LmdbPath, sCar22V7ImagesFolder, sCar22V7JsonFile, sCaffePythonPath, sCar22V7MaskFolder)



    # Negatives
    generateNegativesLmdbFile(sBackgroundLmdbPath, sBackgroundImagesFolder, sBackgroundJsonFile, sCaffePythonPath)
    # generateNegativesLmdbFile(sCarBackgroundLmdbPath, sCarBackgroundImagesFolder, sCarBackgroundJsonFile, sCaffePythonPath)
