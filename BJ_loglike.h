#ifndef BJ_LOGLIKE_H
#define BJ_LOGLIKE_H

#include <vector>

class BJ_loglike {
  public: 
  /**
  * @brief This calss represent an interface to the JUNO Log Likelihood model
  */
  BJ_loglike();

  /**
  * @brief Here we actually calculate the ll
  */
  double ll();

  /**
   * @brief The function we want to fit
   */
  double f(double x);

  /**
   * @brief Generate random sample
   */
  void generateRandom( unsigned int seed);
  // setters and getters for observables and parameters

  void   setPar(int i, double par) { pars[i]=par; }
  double getPar(int i) { return pars[i]; }

  void   setOb(int i, double ob) { obs[i]=ob; } 
  double getOb(int i) { return obs[i]; }

  double getXBin(int i) { return bins_x[i]; }

  // numerical constants

  static const int    BJ_LL_NPARS;
  static const int    BJ_LL_NOBS;
  
  static const double BJ_LL_XMAX;
  static const double BJ_LL_SIGMA;

  static const double BJ_LL_INIT_P0;
  static const double BJ_LL_P0_MIN;
  static const double BJ_LL_P0_MAX;

  static const double BJ_LL_INIT_P1;
  static const double BJ_LL_P1_MIN;
  static const double BJ_LL_P1_MAX;


  private:

  std::vector<double> pars;
  std::vector<double> obs; 

  std::vector<double> bins_x;


};

#endif
