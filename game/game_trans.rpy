################################################################################
## 初始化
################################################################################

init offset = -10

################################################################################
## Ani
################################################################################
transform a:
    alpha 0
    linear 1.5 alpha 1.0

transform b:
    xpos -100
    linear 6 xpos 1350

transform f_w_con:
    xpos f_xpos
    linear 4 xpos tmp_xpos