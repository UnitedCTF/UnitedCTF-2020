package com.filter.mainexample;

/*
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;


@SpringBootApplication(scanBasePackages={"com.filter.*"})
public class SpringMainExample {
    public static void main(final String[] args) {
        final ConfigurableApplicationContext configurableApplicationContext = SpringApplication
                .run(SpringMainExample.class, args);
    }
}

*/

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@SpringBootApplication(scanBasePackages={"com.filter.*"})
public class SpringMainExample {
/*
  @RequestMapping("/")
  public String home() {
    return "Hello Docker World";
  }
*/
  public static void main(String[] args) {
    SpringApplication.run(SpringMainExample.class, args);
 //           final ConfigurableApplicationContext configurableApplicationContext = SpringApplication
   //              .run(SpringMainExample.class, args);

  }

}
