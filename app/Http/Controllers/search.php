<?php

namespace App\Http\Controllers;
use Illuminate\Http\Request;


class search extends Controller
{
      public function read(Request $request){

        $input = (object)$request->all();
        $cat = $input->cat;
        $source=$input->source;
        $inputarr=$input->inputarr;
        $notin=$input->notin;
        $myfile = fopen("storage\test_withoutFR.txt", "r") or die("Unable to open file!");
        $file=fread($myfile,filesize("storage\Stest_withoutFR.txt"));
        fclose($myfile);

        return $file;
      }
}
