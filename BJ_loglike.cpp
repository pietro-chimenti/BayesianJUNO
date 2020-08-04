#include "BJ_loglike.h"

#define _USE_MATH_DEFINES
#include <cmath> 
#include <random>

#include <iostream>


const int    BJ_loglike::BJ_LL_NPARS     = 2;
const int    BJ_loglike::BJ_LL_NOBS      = 100;
const double BJ_loglike::BJ_LL_XMAX      = 10.;
const double BJ_loglike::BJ_LL_INIT_P0   = 0.5;
const double BJ_loglike::BJ_LL_INIT_P1   = 0.;
const double BJ_loglike::BJ_LL_SIGMA     = 1.;

BJ_loglike::BJ_loglike() {

  pars.push_back(BJ_LL_INIT_P0);
  pars.push_back(BJ_LL_INIT_P1);
      
  for(int i = 0; i < BJ_LL_NOBS; i++ ){
    bins_x.push_back((i+1)*BJ_LL_XMAX/BJ_LL_NOBS);
    obs.push_back(f(bins_x[i]));
  }
}

double BJ_loglike::f(double x){
  // just a silly function for now!
  return x*(BJ_LL_XMAX-x)*(1-pars[0]*sin(M_PI*(x/BJ_LL_XMAX+pars[1]))); 
}

double BJ_loglike::ll() {
  double ll = 0;
  for(int i = 0; i < BJ_LL_NOBS; i++)
    ll += (f(bins_x[i])-obs[i])*(f(bins_x[i])-obs[i])/(2*BJ_LL_SIGMA*BJ_LL_SIGMA);
  return ll;
}

void   BJ_loglike::generateRandom( unsigned int seed) {
  // for now just random gaussian fluctuation in each bin
  std::default_random_engine gen(seed);
  std::normal_distribution<double> nd(0.0,BJ_LL_SIGMA);
  for(int i = 0; i < BJ_LL_NOBS; i++)
    obs[i] = f(bins_x[i])+nd(gen);
}


