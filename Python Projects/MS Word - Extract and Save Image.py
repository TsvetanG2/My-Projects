import aspose.words as aw
import os

#automate opens Word document
os.startfile('C:\\Path\\To\\file.docx')

# load the Word document
doc = aw.Document(f"file.docx")

# retrieve all shapes
shapes = doc.get_child_nodes(aw.NodeType.SHAPE, True)
imageIndex = 0
PNGIndex = 0
JPGIndex = 0

# loop through shapes
for shape in shapes :
    shape = shape.as_shape()
    if (shape.has_image) :

        # set image file's name
        imageFileName = f"Image.ExportImages.{imageIndex}_{aw.FileFormatUtil.image_type_to_extension(shape.image_data.image_type)}"

        # save image
        shape.image_data.save(imageFileName)
        imageIndex += 1

    if (shape.has_png) :

        #set png file's name
        PngFileName = f"png.Exportpng.{PNGIndex}_{aw.FileFormatUtil.png_type_to_extension(shape.png_data.png_type)}"

        # save png
        shape.png_data.save(PngFileName)
        PNGIndex += 1

    if (shape.has_jpg):
        # set jpg file's name
        JpgFileName = f"png.Exportjpg.{JPGIndex}_{aw.FileFormatUtil.jpg_type_to_extension(shape.jpg_data.jpg_type)}"

        # save jpg
        shape.png_data.save(JpgFileName)
        JPGIndex += 1