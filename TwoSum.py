def two_sum_list(in_list, req_sum):
    for entry in in_list:
        second_num = req_sum - entry
        if (second_num in in_list) and (second_num!=entry):
            print(str(in_list.index(entry))+ ' and ' + str(in_list.index(second_num)))
            break


two_sum_list(in_list = [2, 7, 11, 15], req_sum = 9)


# Leet Code Submission
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for entry in nums:
            second_num = target - entry
            if second_num in nums:
                return [str(nums.index(entry)),str(nums.index(second_num))]
                # print(str(nums.index(entry))+ ' and ' + str(nums.index(second_num)))
                break
"""
"""
adjudicated_payer_allowed_amount               0
claim_coinsurance_adjustment_amount        36351
claim_copay_adjustment_amount              30225
claim_deductible_adjustment_amount         36306
length_of_stay                              8382
service_count                                  0
total_billed_charge                            0
BPDIASTOLIC                                53218
BPSYSTOLIC                                 53218
Heart/Pulse Rate                           52920
Morse Fall Risk Score                      53049
NIBP Diastolic                             52917
NIBP MAP                                   52972
NIBP MAP Manual Entry                      53214
NIBP Systolic                              52917
PULSE                                      53220
Respiration Rate                           52904
SpO2                                       52986
TEMP                                       53224
Temperature - VS                           52887
Pain Intensity (NRS)                       52889
target                                         0
test_id                                        0
admit_diagnosis_code                           0
admit_diagnosis_primary_display                0
admit_source_code                              0
bill_type_code                                 0
diagnosis_related_group_code                   0
diagnosis_related_group_primary_display        0
frequency_code                                 0
frequency_primary_display                      0
patient_status_primary_display                 0
patient_status_raw_code                        0
payer_claim_number                             0
plan_name                                      0
principal_diagnosis_code                       0
principal_diagnosis_primary_display            0
principal_procedure_primary_display            0
source_description                             0

"""
