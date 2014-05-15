residues_to_fix = ['1', '2', '3', '4', '13', '14', '15', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '40', '41', '42', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '66', '68', '74', '75', '81', '83', '84', '85', '86', '87', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '130', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '169', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '186', '186', '188', '188', '188', '189', '189', '189', '190', '190', '190', '191', '191', '191', '192', '192', '192', '193', '193', '193', '195', '195', '195', '196', '196', '196', '197', '197', '197', '198', '198', '198', '199', '199', '199', '200', '200', '200', '201', '201', '201', '202', '202', '202', '203', '203', '203', '204', '204', '204', '205', '205', '205', '206', '206', '206', '207', '207', '207', '208', '208', '208', '210', '210', '210', '211', '211', '211', '212', '212', '212', '213', '213', '213', '214', '214', '214', '215', '215', '215', '216', '216', '216', '217', '217', '217', '219', '219', '219', '220', '220', '220', '221', '221', '221', '222', '222', '222', '223', '223', '223', '225', '225', '225', '227', '227', '227', '228', '228', '228', '229', '229', '229', '230', '230', '230', '231', '231', '231', '232', '232', '232', '233', '233', '233', '234', '234', '234', '235', '235', '235', '236', '236', '236', '239', '239', '239', '240', '240', '240', '243', '243', '243', '244', '244', '244', '245', '245', '245', '246', '246', '246', '248', '248', '248', '249', '249', '249', '250', '250', '250', '251', '251', '251', '253', '253', '253', '254', '254', '254', '257', '257', '257', '258', '258', '258', '260', '260', '260', '261', '261', '261', '262', '262', '262', '263', '263', '263', '265', '265', '265', '266', '266', '266', '267', '267', '267', '268', '268', '268', '269', '269', '269', '270', '270', '270', '271', '271', '271', '272', '272', '272', '274', '274', '274', '275', '275', '275', '276', '276', '276', '277', '277', '277', '278', '278', '278', '280', '280', '280', '281', '281', '281', '284', '284', '284', '285', '285', '285', '286', '286', '286', '287', '287', '287', '288', '288', '288', '289', '289', '289', '292', '292', '292', '293', '293', '293', '294', '294', '294', '295', '295', '295', '296', '296', '296', '297', '297', '297', '299', '299', '299', '301', '301', '301', '302', '302', '302']
import sys
from os.path import splitext 
opt_dat = open(sys.argv[1], 'r')
opt_val = opt_dat.readlines()
opt_dat.close()
mop_string = ''
tmp_dat = open(sys.argv[1], 'w')
print "Fixing side chains in:", splitext(sys.argv[1])[0]
for line in opt_val:
    if len(line.split()) != 0:
        # '-1' required to discard ')' character from MOPAC residue label
        if line.split()[3][:-1] in residues_to_fix:
            #mop_string += line[:34] + '0' + line[35:50] + '0' + line[51:66] + '0' + line[67:]
            mop_string += line.replace("+1", "+0")
        else:
            mop_string += line
    else:
        mop_string += line
tmp_dat.write(mop_string)
tmp_dat.close()
