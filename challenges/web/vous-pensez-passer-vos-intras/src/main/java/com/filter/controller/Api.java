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
import java.io.FileInputStream;
import javax.servlet.http.HttpServletRequest;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.sql.*;

@RestController
@RequestMapping("/internal")
public class Api {

    @RequestMapping(value = "/getStudent", method = RequestMethod.GET)
    public String getSQL(@RequestParam(name = "name") String name, HttpServletRequest req) {
        StringBuilder sb = new StringBuilder("");
        // System.out.println("name:" + req.getAttribute("name"));
        // System.out.println("param:" + name);
        if (req.getAttribute("name") != null) {
            name = req.getAttribute("name").toString();
        }
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection con = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/ettic?useUnicode=yes&characterEncoding=UTF-8", "ettic", "ettic");
            Statement stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM students WHERE firstname LIKE '%" + name + "%'");
            while (rs.next()) {
                // System.out.println(rs.getInt(1) + "  " + rs.getString(2) + "  " + rs.getString(3));
                sb.append("<br>" + rs.getInt(1) + "  " + rs.getString(2) + "  " + rs.getString(3));
            }
            con.close();
        } catch (Exception e) {
            System.out.println(e);
        }

        return sb.toString();
    }
}
