"""
1. address serializer
2. ParentSerializer
3. StudentSerializer
"""

from rest_framework import serializers
from .models import Student, AcademicFess, Parent
from accounts.models import Address
from accounts.serializers import AddressSerializer


# ================= 2. ParentSerializer =====================


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ['id', 'parent_name', 'parent_date_of_birth', 'parent_nid', 'occupation',
                  'organization_with_designation',
                  'education', 'contact_number', 'parent_email']


# ================= 3. StudentSerializer =====================


class StudentSerializer(serializers.ModelSerializer):
    present_address = AddressSerializer()
    permanent_address = AddressSerializer()
    father_info = ParentSerializer()
    mother_info = ParentSerializer()

    class Meta:
        model = Student
        fields = ['id', 'student_id', 'student_roll_id', 'date_of_birth', 'age', 'birth_certificate', 'student_nid',
                  'passport_number', 'nationality', 'religion', 'gender', 'present_address', 'permanent_address',
                  'father_info', 'mother_info', 'guardian_name', 'guardian_relation', 'guardian_occupation',
                  'yearly_income', 'guardian_contact',
                  'guardian_email', 'other_contact_person', 'other_contact_person_relation',
                  'other_contact_person_contact', 'sibling_id', 'previous_institution_name',
                  'previous_institution_contact',
                  'previous_started_at', 'previous_ending_at', 'previous_ending_class', 'previous_ending_result',
                  'board_exam_name', 'board_exam_registration', 'board_exam_roll', 'board_exam_result',
                  'admitted_department',
                  'admitted_class', 'admitted_group', 'admitted_shift', 'admitted_roll', 'admitted_session',
                  'student_blood_group', 'special_body_sign', 'academic_fees', 'talimi_murobbi_name',
                  'slug']

    def create(self, validated_data):
        present_address = validated_data['present_address']
        permanent_address = validated_data['present_address']
        father_info = validated_data['father_info']
        mother_info = validated_data['father_info']

        date_of_birth = validated_data['date_of_birth']
        admitted_department = validated_data['admitted_department']

        # create address object
        present_address_obj = Address.objects.create(**present_address)
        permanent_address_obj = Address.objects.create(**permanent_address)

        # create parents info
        father_info_obj = Parent.objects.create(**father_info)
        mother_info_obj = Parent.objects.create(**mother_info)

        student = Student.objects.create(date_of_birth=date_of_birth, admitted_department=admitted_department,
                                         present_address=present_address_obj, permanent_address=permanent_address_obj,
                                         father_info=father_info_obj, mother_info=mother_info_obj)
        return student

    def update(self, instance, validated_data):
        present_address = instance.present_address
        permanent_address = instance.permanent_address
        father_info = instance.father_info
        mother_info = instance.mother_info

        # add new value to the form field
        def address_method(varname, validated_value):
            varname.division = validated_data.get(validated_value).get('division', varname.division)
            varname.district = validated_data.get(validated_value).get('district', varname.district)
            varname.thana = validated_data.get(validated_value).get('thana', varname.thana)
            varname.post_office = validated_data.get(validated_value).get('post_office', varname.post_office)
            varname.post_code = validated_data.get(validated_value).get('post_code', varname.post_code)
            varname.address_info = validated_data.get(validated_value).get('address_info', varname.address_info)
            output = varname.save()
            return output

        def parent_info_method(varname, validated_value):
            varname.parent_name = validated_data.get(validated_value).get('parent_name', varname.parent_name)
            varname.parent_date_of_birth = validated_data.get(validated_value).get('parent_date_of_birth', varname.parent_date_of_birth)
            varname.parent_nid = validated_data.get(validated_value).get('parent_nid', varname.parent_nid)
            varname.occupation = validated_data.get(validated_value).get('occupation', varname.occupation)
            varname.organization_with_designation = validated_data.get(validated_value).get('organization_with_designation', varname.organization_with_designation)
            varname.education = validated_data.get(validated_value).get('education', varname.education)
            varname.contact_number = validated_data.get(validated_value).get('contact_number', varname.contact_number)
            varname.parent_email = validated_data.get(validated_value).get('parent_email', varname.parent_email)
            output = varname.save()
            return output

        address_method(present_address, 'present_address')
        address_method(permanent_address, 'permanent_address')
        parent_info_method(father_info, 'father_info')
        parent_info_method(mother_info, 'mother_info')

        # get updated instance value
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.admitted_department = validated_data.get('admitted_department', instance.admitted_department)
        instance.save()
        return instance
