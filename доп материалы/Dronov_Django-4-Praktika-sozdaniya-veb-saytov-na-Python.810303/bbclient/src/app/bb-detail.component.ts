import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { BbService } from './bb.service';

@Component({
  selector: 'app-bb-detail',
  templateUrl: './bb-detail.component.html',
  styleUrls: ['./bb-detail.component.css']
})
export class BbDetailComponent implements OnInit {
  protected bb: any;
  protected comments: any[] = [];

  protected author: String = '';
  protected password: String = '';
  protected content: String = '';

  constructor(private bbservice: BbService,
              private ar: ActivatedRoute) { }

  getComments() {
    this.bbservice.getComments(this.bb.id).subscribe(
        (comments: Object[]) => {this.comments = comments;}
    );
  }

  ngOnInit() {
    const pk = this.ar.snapshot.params['pk'];
    this.bbservice.getBb(pk).subscribe((bb: Object) => {
        this.bb = bb;
        this.getComments();
    });
  }

  submitComment() {
    this.bbservice.addComment(this.bb.id, this.author, this.password,
      this.content).subscribe((comment: Object) => {
        if (comment) {
            this.content = '';
            this.getComments();
        }
      }
    );
  }
}
