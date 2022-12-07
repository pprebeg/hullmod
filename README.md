# hullmod
Ship hull form transformation

1. Install pythonocc using conda
https://github.com/tpaviot/pythonocc-core

conda create -n env_conda_hullmod python=3.9 pythonocc-core=7.6.2 pyside2 -c conda-forge 

2. import iges files with section curves

3. convert section curves wire to bspline
From file:
http://mathlab.github.io/PyGeM/_modules/pygem/cad/cad_deformation.html
use  def _bspline_curve_from_wire(self, wire) to convert wire to bspline curve

4. Calaculate hydrostatic characteristics using section curves      

5. perform Lackenby trasformation

5. perform optimizatio  using Lackenby rules

                                        
