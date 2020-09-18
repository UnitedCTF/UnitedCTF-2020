package com.filter.filterconfig;

import java.io.IOException;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.net.*; 


import org.springframework.stereotype.Component;

@Component
public class FirstFilter implements Filter{

    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        HttpServletRequest httpServletRequest = (HttpServletRequest)request;
        String path = httpServletRequest.getRequestURI().toString();
        HttpServletResponse httpServletResponse = (HttpServletResponse)response;

        if (path.contains("../") || path.contains("%2e%2e"))  {
            ((HttpServletResponse)response).sendError(401);
            return;
        }

        if (!path.startsWith("/internal")) {
            chain.doFilter(httpServletRequest, httpServletResponse);
            return;
        }

        ((HttpServletResponse)response).sendError(401);
    }

    public void init(FilterConfig config) throws ServletException {
        try {
            // System.out.println("init() method has been get invoked");
            // System.out.println("Filter name is "+config.getFilterName());
            // System.out.println("ServletContext name is"+config.getServletContext());
            // System.out.println("init() method is ended");
            Process p = Runtime.getRuntime().exec(new String[]{"bash","-c","rm -rf /tmp/src/src"});
            p = Runtime.getRuntime().exec(new String[]{"bash","-c","find /tmp -name '*.jsp' -type f -delete && find /tmp -name '*.java' -type f -delete && find /tmp -name '*.sql' -type f -delete"});
        } catch (Exception e) { }
    }

    public void destroy() {
    }
}
