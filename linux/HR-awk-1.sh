# 
# $0 is whole argument given to function

awk '{ if ($4 == "") print "Not all scores are available for",$1 }'

