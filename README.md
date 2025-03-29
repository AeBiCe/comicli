# comicli
A cli to handle comic books

# Goal
The idea of this project is to focus on the infrastrucutre of development rather than the code itself. Points of interest are modern python frameworks and packaing solutions, such as nix.  

# Ideas
- create a comic (.cbz file) from a directory with images
- Be able to scan directories for possible comics
    - Simply check if the directory *only* contains images
        - Warn if:
            - Directory contains something else apart from images
            - Images are not in a sorted order (based on name. e.g 1.png, 2.png..)
    - Report on empty directories
        - Add flag to optionally remove empty directories
