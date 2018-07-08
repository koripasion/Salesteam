#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# <meta charset="utf-8">
print("Content-Type:text/html; charset=utf-8\n")
import cgi
form = cgi.FieldStorage()
client = form["customername"].value
customerinfo = form["setuparea"].value
setupdate = form["setupdate"].value



#---------- customer info --------------#

print("<h1>"+"Customer name " + " : " + client+"</h1><br>")
print("Setup Address "+" : "+customerinfo+"<br>")
print("Setup Date " + " : " + setupdate+"<br>")



#---------- Opening --------------#
print("<h2><br>" + "Opening" + "</h2>")

if 'openingsample1' in form:
    openingsample1 = "Opening1"
else :
    openingsample1 = ' '
print("<br>" + openingsample1)

if 'openingsample2' in form:
    openingsample2 = "Opening2"
else :
    openingsample2 = ' '
print("<br>" + openingsample2)

if 'openingsample3' in form:
    openingsample3 = "Opening3"
else :
    openingsample3 = ' '
print("<br>" + openingsample3)

if 'openingsample4' in form:
    openingsample4 = "Opening4"
else :
    openingsample4 = ' '
print("<br>" + openingsample4)

if 'openingsample5' in form:
    openingsample5 = "Opening5"
else :
    openingsample5 = ' '
print("<br>" + openingsample5)

if 'openingsample6' in form:
    openingsample6 = "Opening6"
else :
    openingsample6 = ' '
print("<br>" + openingsample6)

if 'openingsample7' in form:
    openingsample7 = "Opening7"
else :
    openingsample7 = ' '
print("<br>" + openingsample7)





#---------- backgound --------------#
print("<h2><br>" + "Background" + "</h2>")

if 'property template' in form:
    template = "property template"
else :
    template = ' '
print("<br>" + template)

if 'template_1' in form:
    template1 = "template_1"
else :
    template1 = ' '
print("<br>" + template1)

if 'template_2' in form:
    template2 = "template_2"
else :
    template2 = ' '
print("<br>" + template2)

if 'template_3' in form:
    template3 = "template_3"
else :
    template3 = ' '
print("<br>" + template3)

if 'template_4' in form:
    template4 = "template_4"
else :
    template4 = ' '
print("<br>" + template4)

if 'template_5' in form:
    template5 = "template_5"
else :
    template5 = ' '
print("<br>" + template5)

if 'template_6' in form:
    template6 = "template_6"
else :
    template6 = ' '
print("<br>" + template6)

if 'template_7' in form:
    template7 = "template_7"
else :
    template7 = ' '
print("<br>" + template7)

if 'template_erica_1' in form:
    template8 = "template_erica_1"
else :
    template8 = ' '
print("<br>" + template8)

if 'template_erica_2' in form:
    template9 = "template_erica_2"
else :
    template9 = ' '
print("<br>" + template9)



#---------- Environment --------------#
print("<h2><br>" + "LMS requirement" + "</h2>")

if 'LMSsupply' in form:
    LMSrequire = "LMS need"
else :
    LMSrequire = ' '
print("<br>" + LMSrequire)

if 'LMSsupply2' in form:
    LMSrequire2 = "LMS No need"
else :
    LMSrequire2 = ' '
print("<br>" + LMSrequire2)



print("<h2><br>" + "PC requirement" + "</h2>")

if 'PCsupply' in form:
    PCrequire = "Possess PC"
else :
    PCrequire = ' '
print("<br>" + PCrequire)

if 'PCsupply2' in form:
    PCrequire2 = "Snata PC"
else :
    PCrequire2 = ' '
print("<br>" + PCrequire2)

if 'PCsupply3' in form:
    PCrequire3 = "LecturerPC"
else :
    PCrequire3 = ' '
print("<br>" + PCrequire3)



print("<h2><br>" + "PC style" + "</h2>")

if 'PCstyle' in form:
    PCstyle = "Desktop"
else :
    PCstyle = ' '
print("<br>" + PCstyle)

if 'PCstyle2' in form:
    PCstyle2 = "LapTop"
else :
    PCstyle2 = ' '
print("<br>" + PCstyle2)

if 'PCstyle3' in form:
    PCstyle3 = "Possess HDMI"
else :
    PCstyle3 = ' '
print("<br>" + PCstyle3)

if 'PCstyle4' in form:
    PCstyle4 = "Negative HDMi"
else :
    PCstyle4 = ' '
print("<br>" + PCstyle4)





print("<h2><br>" + "Recording style" + "</h2>")

if 'Recordstyle' in form:
    Recordstyle = "During Lecture"
else :
    Recordstyle = ' '
print("<br>" + Recordstyle)

if 'Recordstyle2' in form:
    Recordstyle2 = "only recording"
else :
    Recordstyle2 = ' '
print("<br>" + Recordstyle2)




print("<h2><br>" + "Screen style" + "</h2>")

if 'Screenstyle' in form:
    Screenstyle = "Beam screen"
else :
    Screenstyle = ' '
print("<br>" + Screenstyle)

if 'Screenstyle2' in form:
    Screenstyle2 = "TV"
else :
    Screenstyle2 = ' '
print("<br>" + Screenstyle2)

if 'Screenstyle3' in form:
    Screenstyle3 = "electornic board"
else :
    Screenstyle3 = ' '
print("<br>" + Screenstyle3)

if 'Screenstyle4' in form:
    Screenstyle4 = "blackboard"
else :
    Screenstyle4 = ' '
print("<br>" + Screenstyle4)



print("<h2><br>" + "input style" + "</h2>")

if 'inputstyle' in form:
    inputstyle = "HDMI"
else :
    inputstyle = ' '
print("<br>" + inputstyle)

if 'inputstyle2' in form:
    inputstyle2 = "VGA"
else :
    inputstyle2 = ' '
print("<br>" + inputstyle2)

if 'inputstyle3' in form:
    inputstyle3 = "DVI"
else :
    inputstyle3 = ' '
print("<br>" + inputstyle3)



print("<h2><br>" + "LAN environment" + "</h2>")

if 'Lanenv' in form:
    Lanenv = "Near Computer"
else :
    Lanenv = ' '
print("<br>" + Lanenv)

if 'Lanenv2' in form:
    Lanenv2 = "Far a way"
else :
    Lanenv2 = ' '
print("<br>" + Lanenv2)

if 'Lanenv3' in form:
    Lanenv3 = "no lan"
else :
    Lanenv3 = ' '
print("<br>" + Lanenv3)



print("<h2><br>" + "window environment" + "</h2>")

if 'Windowenv' in form:
    Windowenv = "Nature light"
else :
    Windowenv = ' '
print("<br>" + Windowenv)

if 'Windowenv2' in form:
    Windowenv2 = "No Nature light"
else :
    Windowenv2 = ' '
print("<br>" + Windowenv2)

if 'Windowenv3' in form:
    Windowenv3 = "No window"
else :
    Windowenv3 = ' '
print("<br>" + Windowenv3)
