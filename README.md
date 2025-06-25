# Guython Package Database
Packages for Guython similar to Python's 'pip'.

Here is where you can commit a Pull Request to add packages to the 'gpd' (Guython Package Database) to be used in Guython code files past v1.2.

Guython Packages can be called in Guython code with 'gpd import "gpdPackageName"' and can be used with elements similar to Python with gpdPackageName.Function().

Add your own package with your own function if you wish, ALL packages are scanned to make sure NO malicious code is being executed, packages are written in either Guython or Python.

GPD Packages ***MUST*** be unecrypted and open source.

***PLEASE test and verify your package works properly with Guython before uploading!***
***You can add your package to your local Guython 'packages' folder to test!***

# How to make your own package
Making your own Guython package is very simple.
1. Create your own directory
   - This is the name of your package, and what it will be called in the GPD index.
   - All of your package files will go in here.
2. Add a 'manifest.gy' file
   - All packages require this file, as its what tell the index the name, your main file, and what language it is built in.
3. Choose a language
   - Guython packages can be writtten in Guython or Python.
   - Python packages are easier to make, but more restricted.
4. Add your files
   - Once your '.gy' or '.py' files are added, you are done!
5. Upload here
   - Fork the repo and upload your new package there.
   - Submit your fork as a pull request so everything can be verifyed and added.
  
# We Need Packages!
We really need some more packages for Guython! If you have the skill, please add your ideas!
