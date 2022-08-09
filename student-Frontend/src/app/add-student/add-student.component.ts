import { Component, OnInit } from '@angular/core';
import { ServicesService } from '../services.service';
import { Studentdetails ,District } from '../models/student.model';
@Component({
  selector: 'app-add-student',
  templateUrl: './add-student.component.html',
  styleUrls: ['./add-student.component.scss']
})
export class AddStudentComponent implements OnInit {
  Student: Studentdetails = {

    reg_no: '',
    stud_name:'',
    gender: '',
    date_of_join: '',
    address: '',
    dist_id: undefined,
  };
  dist?: District[];

  submitted = false;
  constructor(private ServicesService: ServicesService) { }

  ngOnInit(): void {

    this.retrieveDist();
  }
  retrieveDist(): void {
    this.ServicesService.getdist()
      .subscribe(
        data => {
          this.dist = data;
          console.log(data, 'dist');
        },
        error => {
          console.log(error);
        });
  }
  saveStudent(): void {

    const data = {
      'stud_name': this.Student.stud_name,
      'reg_no': this.Student.reg_no,
      'gender': this.Student.gender,
      'date_of_join': this.Student.date_of_join,
      'address': this.Student.address,
      'dist_id': Number(this.Student.dist_id)
    };
    console.log(data)
    if (data.stud_name == '') {
      alert('Name cannot be empty')
      return
    } if (data.reg_no == '') {
      alert('Registration cannot be empty')
      return
    } if (data.gender == '') {
      alert('Select gender')
      return
    } if (data.date_of_join == '') {
      alert('Date of birth cannot be empty')
      return
    } if (data.address == '') {
      alert('Address cannot be empty')
      return
    } if (data.dist_id == undefined) {
      alert('Select district')
      return
    }
    console.log(this.Student, 'Student')
    this.ServicesService.post(data)
      .subscribe(
        response => {
          console.log(response);
          if (response.status == 0) {
            this.submitted = false
            alert('Invalid Registration Number')
          }
          else {
            this.submitted = true
          }
        },
        error => {
          console.log(error);
        });
  }
  // newStudent(): void {
  //   this.submitted = false;
  //   this.Student = {
  //     stud_name: '',
  //     reg_no: '',
  //     gender: '',
  //     date_of_join: '',
  //     address: '',
  //     dist_id: 0
  //   };

  // }

}
