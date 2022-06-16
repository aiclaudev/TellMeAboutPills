# extracting bounding box axis
def extractxyxy(xyxy) : 
    return [int(xyxy[0].item()), int(xyxy[1].item()), int(xyxy[2].item()), int(xyxy[3].item())]