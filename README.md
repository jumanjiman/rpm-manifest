# A simple approach for comparing host builds #

This package uses a simple RPM query to generate a hash, or
_rpm-manifest_, of the set of RPMs installed on a given host. The
manifest is deterministic, so:

* If two hosts have the _same_ manifest, those two 
  hosts have the _same_ combination of RPMs, including
  epoch, name, version, and release.

* If two hosts have _different_ manifests, those two
  hosts have a _different_ combination of RPMs.

IMPORTANT: An rpm-manifest is _not_ a tool for comparing
configuration files or detecting intrusions.

## Sample Use Cases ##

### Kickstart verification ###

If you compute the rpm-manifest for a given kickstart,
you can compare the actual manifest during `%post` to
the expected manifest as a *go-no-go* check of the build.

### Change detection ###

Given a set of hosts, has anybody changed the build
by updating, installing, or removing RPMs?

The following output shows the manifests for each
host in the set, clearly identifying the hosts
that have been modified.

```
pc-pp01a : ad52c23663e76c4eb7cee27c0d3613ab
pc-pp01b : f65b8d62011ec3ab59ac816a088e7c0a
pc-pp02a : 6422646db863598ea705a1e5806f5b08
pc-pp02b : baa1e43c95dd58cd367ab289fe042d67
pc-pp03a : baa1e43c95dd58cd367ab289fe042d67
pc-pp03b : baa1e43c95dd58cd367ab289fe042d67
pc-pp04a : baa1e43c95dd58cd367ab289fe042d67
pc-pp04b : baa1e43c95dd58cd367ab289fe042d67
pc-pp05a : baa1e43c95dd58cd367ab289fe042d67
pc-pp05b : baa1e43c95dd58cd367ab289fe042d67
pc-pp06a : baa1e43c95dd58cd367ab289fe042d67
pc-pp06b : baa1e43c95dd58cd367ab289fe042d67
pc-pp07a : 5a67d2db48b5396968bac87c631bbb98
pc-pp07b : 89a1f692b9659a5928413c56213b0c95
pc-pp08a : baa1e43c95dd58cd367ab289fe042d67
pc-pp08b : baa1e43c95dd58cd367ab289fe042d67
pc-pp09a : baa1e43c95dd58cd367ab289fe042d67
pc-pp09b : baa1e43c95dd58cd367ab289fe042d67
```
