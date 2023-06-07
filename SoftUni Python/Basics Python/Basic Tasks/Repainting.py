NylonPerMeter = 1.50
PaintingPerLitre = 14.50
SeparatorPerLitre = 5.00

NylonNeeded = int(input())
PaitingLetresNeeded = int(input())
SeparatorLitresNeeded = int(input())
Hours = int(input())

NylonSum = (NylonNeeded + 2) * NylonPerMeter
PaintingSum = PaitingLetresNeeded * PaintingPerLitre;
RumensAddPaint = PaintingSum + (PaintingSum * 0.10)
SeparatorSum = SeparatorLitresNeeded * SeparatorPerLitre
Bags = 0.40

ResultMaterials = NylonSum + RumensAddPaint + SeparatorSum + Bags
ResultWork = (ResultMaterials * 0.30) * Hours
FinalResult = ResultWork + ResultMaterials
print(FinalResult)
