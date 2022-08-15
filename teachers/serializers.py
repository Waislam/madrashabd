from rest_framework import serializers
from .models import Teacher, Education, Skill
from students.serializers import AddressSerializer
from accounts.models import Address


class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = ['id', 'degree_name', 'institution_name', 'passing_year', 'result']


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ['id', 'skill_name']


class TeacherSerializer(serializers.ModelSerializer):
    present_address = AddressSerializer()
    permanent_address = AddressSerializer()
    education = EducationSerializer()
    skill = SkillSerializer()


    class Meta:
        model = Teacher
        fields = ['id', 'teacher_id', 'father_name', 'mother_name', 'date_of_birth', 'gender', 'religion',
                  'marital_status', 'present_address', 'permanent_address', 'education', 'skill',
                  'phone_home', 'nid', 'birth_certificate', 'nationality', 'blood_group', 'department',
                  'designation', 'starting_date', 'ending_date', 'slug']

    def create(self, validated_data):
        present_address = validated_data['present_address']
        permanent_address = validated_data['permanent_address']
        education = validated_data['education']
        skill = validated_data['skill']

        present_address_obj = Address.objects.create(**present_address)
        permanent_address_obj = Address.objects.create(**permanent_address)

        education_obj = Education.objects.create(**education)
        skill_obj = Skill.objects.create(**skill)

        # now create teacher obj
        phone_home = validated_data['phone_home']
        nid = validated_data['nid']
        birth_certificate = validated_data['birth_certificate']

        teacher = Teacher.objects.create(phone_home=phone_home, nid=nid, birth_certificate=birth_certificate,
                                         present_address=present_address_obj, permanent_address=permanent_address_obj,
                                         education=education_obj, skill=skill_obj)
        return teacher

    def update(self, instance, validated_data):
        # get all nested obj
        present_address = instance.present_address
        permanent_address = instance.permanent_address
        education = instance.education
        skill = instance.skill

        # get updated fields value for every nested obj
        def address_method(varname, validated_value):
            varname.division = validated_data.get(validated_value).get('division', varname.division)
            varname.district = validated_data.get(validated_value).get('district', varname.district)
            varname.thana = validated_data.get(validated_value).get('thana', varname.thana)
            varname.post_office = validated_data.get(validated_value).get('post_office', varname.post_office)
            varname.post_code = validated_data.get(validated_value).get('post_code', varname.post_code)
            varname.address_info = validated_data.get(validated_value).get('address_info', varname.address_info)
            output = varname.save()
            return output

        address_method(present_address, 'present_address')
        address_method(permanent_address, 'permanent_address')

        education.degree_name = validated_data.get('education').get('degree_name', education.degree_name)
        education.institution_name = validated_data.get('education').get('institution_name', education.institution_name)
        education.passing_year = validated_data.get('education').get('passing_year', education.passing_year)
        education.result = validated_data.get('education').get('result', education.result)
        education.save()

        skill.skill_name = validated_data.get('skill').get('skill_name', skill.skill_name)
        skill.save()

        instance.phone_home = validated_data.get('phone_home', instance.phone_home)
        instance.nid = validated_data.get('nid', instance.nid)
        instance.birth_certificate = validated_data.get('birth_certificate', instance.birth_certificate)
        instance.save()
        return instance
