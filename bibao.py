# conding:utf-8
def pass_line(line):
    def com(val):
        if val >= line:
            print 'pass'
        else:
            print 'fail'
    return com


line_90 = pass_line(90)
line_90(89)
line_90(90)

line_100 = pass_line(100)
line_100(100)
line_100(90)





