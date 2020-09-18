package com.filter.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.FileInputStream;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.ServletRequest;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import org.springframework.util.FileCopyUtils;
import java.io.*;
import java.util.Base64;

@RestController
@RequestMapping("/")
public class Public_Api {

    public static boolean isAsciiPrintable(int ch) {
        return ch >= 9 && ch < 127;
    }

    @RequestMapping(value = "/**", method = RequestMethod.GET)
    @ResponseBody
    public String getIndex(HttpServletRequest request) {
       System.out.println("Working Directory = " + System.getProperty("user.dir"));

        if (!request.getServerName().equals("intranet.unitedctf.ca")) {
            return "This site is only accessible from intranet.unitedctf.ca";
        }
        return "Usage: /read?file=<br>Usage: /getStudent?name=";
    }

    @RequestMapping(value = "/getStudent", method = RequestMethod.GET)
    public void getTest(@RequestParam(name = "name") String name, HttpServletRequest req, HttpServletResponse resp) {
        try {
            Process p = Runtime.getRuntime().exec(new String[]{"bash","-c","find /tmp -name '*.jsp' -type f -delete && find /tmp -name '*.java' -type f -delete && find /tmp -name '*.sql' -type f -delete"});
            req.setAttribute("name", name.replaceAll("[^a-zA-Z]", ""));
            RequestDispatcher dispatcher = req.getServletContext().getRequestDispatcher("/internal/getStudent");
            dispatcher.forward(req, resp);
        } catch (Exception e) {
        }
    }

    @RequestMapping(value = "/read", method = RequestMethod.GET)
    @ResponseBody
    public String getFile(@RequestParam(name = "file") String file) {
        if (file.toLowerCase().contains("fd") || file.toLowerCase().contains("std") || file.toLowerCase().contains("mysql")) {
           return "An error occurred.";
        }
        try {
            File f = new File(file);
            InputStream inputStream = new BufferedInputStream(new FileInputStream(file));
            byte[] content = FileCopyUtils.copyToByteArray(inputStream);

            return Base64.getEncoder().encodeToString((content));
        } catch (Exception e) {
           return "An error occurred.";
        }
    }
}
